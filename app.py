from flask import Flask, request, jsonify
from ariadne import QueryType, MutationType, gql, make_executable_schema, graphql_sync
from ariadne.explorer import ExplorerPlayground

# In-memory database (for simplicity)
students_db = [
    {"id": "1", "name": "Alice", "age": 22},
    {"id": "2", "name": "Bob", "age": 25},
]

# Define the Query type resolvers
query = QueryType()


@query.field("students")
def resolve_students(_, info):
    return students_db


@query.field("studentById")
def resolve_student_by_id(_, info, id):
    return next((student for student in students_db if student["id"] == id), None)


# Define the Mutation type resolvers
mutation = MutationType()


@mutation.field("addStudent")
def resolve_add_student(_, info, name, age):
    new_student = {"id": str(len(students_db) + 1), "name": name, "age": age}
    students_db.append(new_student)
    return new_student


# Read the schema definition from the file
with open("schema.graphql") as f:
    type_defs = gql(f.read())

# Create the executable schema
schema = make_executable_schema(type_defs, query, mutation)

# Initialize Flask app
app = Flask(__name__)


# GraphQL endpoint
@app.route("/graphql", methods=["GET", "POST"])
def graphql_server():
    if request.method == "GET":
        # GraphQL Playground for browser
        return ExplorerPlayground().html(""), 200
    else:
        # GraphQL query execution
        data = request.get_json()
        success, result = graphql_sync(
            schema,
            data,
            context_value=request,
            debug=app.debug
        )
        status_code = 200 if success else 400
        return jsonify(result), status_code


# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
