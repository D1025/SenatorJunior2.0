import time

def feedback(ctx, text):
    with open("feedback/feedback.txt", 'a') as file:
        file.write("".join([str(time.time), " - ", str(ctx.author), " - ", text]))
        