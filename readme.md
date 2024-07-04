# Order Cloth by Rasa.ai

## Installation

1. Create a new virtual environment by choosing a Python interpreter and making a `./venv`:
    ```bash
    python3 -m venv ./venv
    ```

2. Activate the virtual environment:
    ```bash
    source ./venv/bin/activate
    ```

3. Install `rasa-pro` with:
    ```bash
    pip install uv
    uv pip install rasa-pro --extra-index-url=https://europe-west3-python.pkg.dev/rasa-releases/rasa-pro-python/simple/
    ```

## Initialize Project

1. Clone this project:
    ```bash
    mkdir order-cloth-by-rasa.ai
    cd order-cloth-by-rasa.ai
    git clone https://github.com/putra-asmarjoe/order-cloth-by-rasa.ai.git .
    ```

2. Enable Redis to store the tracker:
    ```bash
    docker run -d --name my-redis-stack -p 6379:6379 -v /Users/my-redis/:/data -e REDIS_ARGS="--requirepass MY_SECURE_PASS --appendonly yes" redis/redis-stack-server:latest
    ```
    *You can disable Redis in `endpoints.yml` if not needed.*

## Running the App

1. Build the model:
    ```bash
    rasa train
    ```

2. Run custom actions:
    ```bash
    rasa run actions
    ```

3. To interact with the shell mode:
    ```bash
    rasa shell
    ```

4. To run interactive mode:
    ```bash
    rasa interactive
    ```

5. Run the model:
    ```bash
    rasa run --enable-api --cors="*" --port 5005
    ```

6. To launch the web UI for inspection:
    ```bash
    rasa inspect
    ```
 
## NLU Flow

The NLU flow for the chatbot is as follows:

1. **Initial greeting**: The bot greets the user and asks how it can assist.
2. **Specify product type**: The user specifies the type of product they want to order (e.g., tshirt or jeans).
3. **Specify size**: The bot asks for the size of the product.
4. **Specify color**: The bot asks for the color of the product.
5. **Confirm order**: The bot confirms the order details and asks the user for confirmation.

Here is an example interaction:

1. **User**: Hi
   - **Bot**: What type of product would you like to order? Please specify.

2. **User**: I want to buy jeans
   - **Bot**: What size do you need? Please specify.

3. **User**: Small is good for me
   - **Bot**: What color would you like? Please specify.

4. **User**: Black is fine
   - **Bot**: Do you want to confirm your order for jeans in size small and color Black?

5. **User**: Yes
   - **Bot**: Your order for jeans in size small and color Black has been received. Thank you!

This flow ensures a structured and guided interaction for placing orders.

## Using Endpoints to Send Chat

1. Initial greeting:

    ```sh
    curl -XPOST http://localhost:5005/webhooks/rest/webhook -d '{"sender": "user", "message": "Hi"}'
    ```

    Response:

    ```json
    [{"recipient_id":"user","text":"What type of product would you like to order? Please specify."}]
    ```

2. Specify product type:

    ```sh
    curl -XPOST http://localhost:5005/webhooks/rest/webhook -d '{"sender": "user", "message": "I want to buy jeans"}'
    ```

    Response:

    ```json
    [{"recipient_id":"user","text":"What size do you need? Please specify."}]
    ```

3. Specify size:

    ```sh
    curl -XPOST http://localhost:5005/webhooks/rest/webhook -d '{"sender": "user", "message": "Small is good for me"}'
    ```

    Response:

    ```json
    [{"recipient_id":"user","text":"What color would you like? Please specify."}]
    ```

4. Specify color:

    ```sh
    curl -XPOST http://localhost:5005/webhooks/rest/webhook -d '{"sender": "user","message": "black is fine"}'
    ```

    Response:

    ```json
    [{"recipient_id":"user","text":"Do you want to confirm your order for jeans in size small and color black?"}]
    ```

5. Confirm order:

    ```sh
    curl -XPOST http://localhost:5005/webhooks/rest/webhook -d '{"sender": "user","message": "yes"}'
    ```

    Response:

    ```json
    [{"recipient_id":"user","text":"Your order for jeans in size small and color black has been received. Thank you!"}]
    ```
## Running the Widget on Your Website

You can run the widget on your website using the following code:

```html
<div id="rasa-chat-widget" data-websocket-url="http://localhost:5005/"></div>
<script src="https://unpkg.com/@rasahq/rasa-chat" type="application/javascript"></script>