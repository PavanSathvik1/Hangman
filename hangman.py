import random
words = [
    {"word":"banana","hint":"A yellow fruit rich in potassium"},
    {"word":"car","hint":"A four-wheeled vehicle"},
    {"word":"river","hint":"A natural flowing water body"},
    {"word":"moon","hint":"Earth's natural satellite"},
    {"word":"pen","hint":"A tool for writing"},
    {"word":"chair","hint":"Furniture used for sitting"},
    {"word":"train","hint":"A rail-based transport"},
    {"word":"ocean","hint":"A vast body of salt water"},
    {"word":"star","hint":"A luminous celestial object"},
    {"word":"notebook","hint":"A collection of writable pages"},
    {"word":"glass","hint":"A transparent material or container"},
    {"word":"pineapple","hint":"A tropical fruit with spiky skin"},
    {"word":"bus","hint":"A large vehicle for public transport"},
    {"word":"park","hint":"An open area for recreation"},
    {"word":"earth","hint":"The planet we live on"},
    {"word":"table","hint":"Furniture with a flat surface"},
    {"word":"bike","hint":"A two-wheeled vehicle"},
    {"word":"desert","hint":"A dry, sandy region"},
    {"word":"planet","hint":"A celestial body orbiting a star"},
    {"word":"journal","hint":"A book for daily entries"},
    {"word":"mug","hint":"A container for drinking liquids"},
    {"word":"strawberry","hint":"A small red fruit with seeds"},
    {"word":"airplane","hint":"A flying vehicle"},
    {"word":"island","hint":"Land surrounded by water"},
    {"word":"galaxy","hint":"A system of stars and planets"},
    {"word":"dictionary","hint":"A book of word meanings"},
    {"word":"bowl","hint":"A round dish for holding food"},
    {"word":"grape","hint":"A small juicy fruit"},
    {"word":"ship","hint":"A large water-based transport"},
    {"word":"mountain","hint":"A high landform"},
    {"word":"comet","hint":"A celestial object with a tail"},
    {"word":"tablet","hint":"A portable computing device"},
    {"word":"cup","hint":"A small container for beverages"},
    {"word":"orange","hint":"A citrus fruit rich in vitamin C"},
    {"word":"scooter","hint":"A two-wheeled motor vehicle"},
    {"word":"lake","hint":"A water body surrounded by land"},
    {"word":"cloud","hint":"A mass of water vapor in the sky"},
    {"word":"encyclopedia","hint":"A book of comprehensive knowledge"},
    {"word":"jug","hint":"A container with a handle and spout"},
    {"word":"pear","hint":"A green or yellow fruit"},
    {"word":"submarine","hint":"A water vehicle that goes underwater"},
    {"word":"forest","hint":"A large area with dense trees"},
    {"word":"asteroid","hint":"A small rocky celestial body"},
    {"word":"camera","hint":"A device for capturing photos"},
    {"word":"can","hint":"A cylindrical container"},
    {"word":"peach","hint":"A sweet fruit with fuzzy skin"},
    {"word":"helicopter","hint":"An aerial vehicle with rotors"},
    {"word":"waterfall","hint":"A stream of water falling from height"},
    {"word":"nebula","hint":"A cloud of gas in space"},
    {"word":"diary","hint":"A personal record of experiences"},
    {"word":"pitcher","hint":"A large container for liquids"},
    {"word":"kiwi","hint":"A small brown fruit with green flesh"},
    {"word":"jeep","hint":"A rugged off-road vehicle"},
    {"word":"cave","hint":"A natural underground space"},
    {"word":"sunflower","hint":"A yellow flower that follows the sun"},
    {"word":"atlas","hint":"A book of maps"},
    {"word":"bucket","hint":"A round container with a handle"},
    {"word":"mango","hint":"A juicy tropical fruit"},
    {"word":"tram","hint":"A rail vehicle for urban areas"},
    {"word":"valley","hint":"A low area between hills or mountains"},
    {"word":"constellation","hint":"A group of stars forming a pattern"},
    {"word":"novel","hint":"A long fictional story"},
    {"word":"pan","hint":"A shallow cooking container"},
    {"word":"plum","hint":"A small, sweet purple fruit"},
    {"word":"rocket","hint":"A vehicle that travels to space"},
    {"word":"volcano","hint":"A mountain with lava"},
    {"word":"solar","hint":"Related to the Sun"},
    {"word":"magazine","hint":"A periodical publication"},
    {"word":"thermos","hint":"A container that retains temperature"},
    {"word":"apple","hint":"A red or green fruit"},
    {"word":"van","hint":"A medium-sized transport vehicle"},
    {"word":"cliff","hint":"A steep rock face"},
    {"word":"rainbow","hint":"A multicolored arc in the sky"},
    {"word":"telescope","hint":"An instrument to observe space"},
    {"word":"comic","hint":"A book with illustrated stories"},
    {"word":"bottle","hint":"A container for liquids"},
    {"word":"blueberry","hint":"A small blue fruit"},
    {"word":"taxi","hint":"A vehicle for hire"},
    {"word":"pond","hint":"A small water body"},
    {"word":"meteor","hint":"A space rock entering the atmosphere"},
    {"word":"calendar","hint":"A chart of dates"},
    {"word":"kettle","hint":"A container for boiling water"},
    {"word":"melon","hint":"A large juicy fruit"},
    {"word":"yacht","hint":"A luxury watercraft"},
    {"word":"glacier","hint":"A moving mass of ice"},
    {"word":"aurora","hint":"Natural lights in polar regions"},
    {"word":"storybook","hint":"A book of tales"},
    {"word":"plate","hint":"A flat dish for serving food"},
    {"word":"lime","hint":"A green citrus fruit"},
    {"word":"cruise","hint":"A ship for leisure trips"},
    {"word":"canyon","hint":"A deep valley with steep sides"},
    {"word":"eclipse","hint":"An astronomical event"},
    {"word":"catalog","hint":"A list of items"},
    {"word":"pitcher","hint":"A container for pouring liquids"}
]


def main():
    while True:
        a = choice()
        if a == 1:
            limited()
            break
        elif a == 2:
            unlimited()
            break
        else:
            print("Enter either 1 or 2")


def choice():
    while True:
        try:
            choice = int(input("Enter any one of these : \n1: Limited (You will get a choice to select number of words you want to play)\n2: Unlimited (You can play until you lose) \n Select your choice 1 or 2: "))
            break
        except IndexError:
            print("Enter a number")
    return choice


def limited():
    while True:
        try:
            num = int(input("Enter the number of words you want to play : "))
            break
        except ValueError:
            print("Enter a number")
    count= 0
    for i in range(num):
        c = game()
        if c == 1:
            count += 1
    print(f"Your score is : {count}")
        

def unlimited():
    count = 0
    c = 1
    while c==1:
        c = game()
        if c == 1:
            count+= 1
    print(f"You have played {count} words")


def game():

    a = random.choice(words)
    word = a["word"]
    b = "".join(["_" for letter in word])
    words.remove(a)

    print(b)
    print(a["hint"])
    n = 0
    c = 0
    while n<6:
        z = 0
        guess = input("Enter a letter . If you are entering more than 1 letter it will be considered as a word and checked . Enter your guess : ")
        if len(guess) == 1:
            for i in range(len(word)):
                if guess == word[i]:
                    b = b[:i]+guess+b[i+1:]
                    z = 1
                else:
                    if z==1:
                        continue
                    elif word[i] == word[-1]:
                        n = n+1
                        print(f"You have {6-n} chances left")
            print(b)
        elif len(guess) == 0:
            print("Enter a guess")
        else:
            if guess == a["word"]:
                print("The guess is correct")
                c = 1
                return c
            else:
                print("The guess is wrong")
                return c

        if b == word:
            print("You have guessed the correct word... ")
            c = 1
            return c
               

if __name__ == "__main__":
    main()
