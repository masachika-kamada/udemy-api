# Rest API tutorial

Udemy course URL: <https://www.udemy.com/course/rest-api-flask-and-python/>

Interact with and test REST API: use insomnia

## Docker

```bash
docker build -t rest-api-tutorial .
docker run -p 5000:5000 -w /app -v "$(pwd):/app" rest-api-tutorial
```

## Docker compose

```bash
docker-compose up
docker-compose up --build --force-recreate --no-deps web
```

## Notes

* `.flaskenv` file is used to set environment variables for Flask
* When API receives a request from a client, marshmallow is used to validate the request data<br>
    **Before marshmallow**
    ```python
    def post(self):
        store_data = request.get_json()
        if "name" not in store_data:
            abort(400, message="Bad request. Ensure 'name' is included in the JSON payload.")
    ```
    **After marshmallow**
    ```python
    @blp.arguments(ItemSchema)
    def post(self, item_data):
* Accessing <http://127.0.0.1:5000/swagger-ui/> will show the API documentation
* HTTP status codes
    | Code | Description |
    | --- | --- |
    | 200 | OK |
    | 201 | Created |
    | 400 | Bad Request |
    | 404 | Not Found |
* `lazy` is an argument for `SQLAlchemy.relationship()`, which controls how related data is loaded.
    * `lazy="dynamic"` returns a query object for relationships, allowing dynamic filtering and sorting. This query object behaves like a class instance:
        ```python
        store = StoreModel.query.get(store_id)
        items_query = store.items.filter(ItemModel.price > 20)
        filtered_items = items_query.all()
        ```
    * `lazy="select"` immediately loads relationships as a list, without dynamic query capabilities:
        ```python
        store = StoreModel.query.get(store_id)
        items = store.items  # items is a list
        ```
    * `lazy="joined"` and `lazy="subquery"` load related data using JOIN and subquery SQL statements, respectively.
    * There are other variations such as `lazy="immediate"`, etc.
