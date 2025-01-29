frown = "🙁"
happy = "🙂"

def convert(face):
    replace_happy = face.replace(":)", happy)
    new_face = replace_happy.replace(":(", frown)
    return new_face

def main():
    face = input("enter the string with a face: ")
    face_with_emoji = convert(face)
    print(face_with_emoji)

main()


