INDENTS = 4

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


def print_hanging_indents(poem):
    lineCount = 0

    lines = poem.split('\n')
    for line in lines:
        line = line.strip()

        if not line:
            lineCount = 0
            continue
        else:
            lineCount += 1

        newLine = (' ' * INDENTS) if lineCount is not 1 else ''
        print(newLine + line)


# def print_hanging_indents(poem):
#     """You can use textwrap's fill but this worked better for us"""
#     for part in poem.split("\n\n"):
#         lines = [line.strip() for line in part.splitlines()
#                  if line.strip()]
#         print(lines[0])
#         for line in lines[1:]:
#             print(' ' * INDENTS + line)


if __name__ == '__main__':
    print_hanging_indents(rosetti_unformatted)
