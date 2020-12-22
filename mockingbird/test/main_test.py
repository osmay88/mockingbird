from mockingbird.main import create_stub


def test_print_hello():
  new_stub = {
    "body": {
      "request": {
        "method": "GET",
        "url": "/some/thing"
      },
      "response": {
        "status": 200,
        "body": "Hello world!",
        "headers": {
          "Content-Type": "text/plain"
        }
      }
    }
  }

  response = create_stub(new_stub, None)
  print(response)
