from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/items/")
def create_item(item):
    print("tested")
    # if not item.data:
    #     raise HTTPException(status_code=400, detail="Data not provided")
    # # Do something with item.data
    return item

# @app.route('/ask', methods=['POST'])
# def post_example():
#     # Get JSON data from the request
#     content = request.json
#
#     # Print received data
#     print(content)
#
#     # Respond back
#     return jsonify({"message": "Data received!"})

# @app.post('/ask')
