# 200 to 299 ok
# 400 to 499 not found error
# 500 to 599 internal error
def http_status(num):
    match num:
        case 200:
            return "ok"
        case 400:
            return "not found error"
        case 500:
            return "internal error"
        case _:
            return "unknown error"
print(http_status(200))