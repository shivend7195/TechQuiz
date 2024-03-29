print("********************************************************************************")

print(">>>>>>>>>>>>>>>>>>>>>>>*!TECHTWIST TRIVIA!*<<<<<<<<<<<<<<<<<<<<<<<")

print("********************************************************************************")
question = 1
score = 0
while(question <= 10):
    if question == 1:
        print("1. Who is the founder of cred:")
        print("a) kunal shah           b) kamath brothers ")
        solution = (input("whats the correct option: "))
        if solution == "a":
            score += 10
        else:
            break
    elif question == 2:
        print("2. James Gosling invented the programming language:")
        print("a) Haskell           b) JAVA ")
        solution = (input("what's the correct option: "))
        if solution == "b":
            score += 10
        else:
            break
    elif question == 3:
        print("3. Abbreviation of QR in QR code:")
        print("a) Quality Read           b) Quick Response ")
        solution = (input("what's the correct option: "))
        if solution == "b":
            score += 10
        else:
            break
    elif question == 4:
        print("4. Which company introduced the first commercially available smartphone:")
        print("a) IBM           b) Apple Inc. ")
        solution = (input("what's the correct option: "))
        if solution == "a":
            score += 10
        else:
            break
    elif question == 5:
        print("5. What was the original name of Google search engine before it was renamed:")
        print("a) Backrub           b) Webcrawler ")
        solution = (input("what's the correct option: "))
        if solution == "a":
            score += 10
        else:
            break
    elif question == 6:
        print("6. Who coined the term (Virtual Reality):")
        print("a) Ivan Sutherland           b) Jaron Lanier ")
        solution = (input("what's the correct option: "))
        if solution == "b":
            score += 10
        else:
            break
    elif question == 7:
        print("7. The first Computer Virus to infect Microsoft Windows:")
        print("a) ILOVEYOU           b) Brain ")
        solution = (input("what's the correct option: "))
        if solution == "b":
            score += 10
        else:
            break
    elif question == 8:
        print("8. Who often regarded as World's first computer programmer:")
        print("a) Ada Lovelace           b) Charles Babbage ")
        solution = (input("what's the correct option: "))
        if solution == "a":
            score += 10
        else:
            break
    elif question == 9:
        print("9. What is the name of the first consumer-grade virtual reality headset released in 2016:")
        print("a) Oculus Rift           b) HTC Vive ")
        solution = (input("what's the correct option: "))
        if solution == "b":
            score += 10
        else:
            break
    elif question == 10:
        print("10. Which is not a cloud computing service provided by (AWS):")
        print("a) EC2 (Elastic Compute Cloud)           b) P2P (Peer-to-Peer) ")
        solution = (input("what's the correct option: "))
        if solution == "b":
            score += 10
        else:
            break
        
    question +=1

print("**********************************************************************************")

if score == 0:
    print("oops! the score is 0, you must be little uncomfortable with tech world :|")
elif score > 0 and score <= 50:
    print("OH! selective engagment? you scored ",score)
elif score > 50 and score < 100:
    print("you are confident, you nailed",score)
else :
    print("perfect 100! Are you IRON MAN ")
    

print("KEEP LEARNING :)")