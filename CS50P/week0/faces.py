def main():
    face_word = input("Enter your texts with emotions: ")

    face_word = face_word.replace(':)', '😁')
    face_word = face_word.replace(':(', '😟')

    print(face_word)

main()