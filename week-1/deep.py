answer = input("What is the Great Question of Life, the Universe and Everything? ")
formatted_answer = answer.lower()

def forty_two(answer):
    if answer.replace(" ", "") == "42":
        return "42"
    else:
        return answer


final = forty_two(formatted_answer)
match formatted_answer:
    case "forty-two" | "forty two":
        print("Yes")
    case "42":
        print("Yes")
    case _:
        print("No")

