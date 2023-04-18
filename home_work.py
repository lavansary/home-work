# Домашние задание №1

@app.route("/quotes/<int:quote_id>", methods=['DELETE'])
def delete_quote(quote_id):
    for quote in quotes:
        if quote["id"] == quote_id:
            #TODO: реализовать удаление цитаты из списка
            return f"Quote with id {id} is deleted.", 204
    return  f"Quote with id={quote_id} not found" 404


    # Домашние задание №2

    #TODO: реализация метода PUT для изменения существующей цитаты в репозитории

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        for quote in ai_quotes:
            if (id == quote["id"]):
                quote["author"] = params["author"]
                quote["quote"] = params["quote"]
                return quote, 200
        quote = {
            "id": id,
            "author": params["author"],
            "quote": params["quote"]
        }
        ai_quotes.append(quote)
        return quote, 201