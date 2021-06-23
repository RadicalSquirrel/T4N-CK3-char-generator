# Step 1: Download Python 3.9
# Step 2: Download pycharm
# step 3: Open this with pycharm
# step 4: go to view->python packages and install numpy and matplotlib
# step 5: right click on the code and hit run

# Made by Lisain
# Expanded by TypicalCrusader
# Updated for Publishing by RadSquirrel
# Python 3

import numpy as np
import random
import matplotlib.pyplot as plt
from string import Template
import sys, os


# Create Database of everything

# Its not the cleanest way to implement this but well it works - Typical

# TODO Write a program which will rip code names of traits, faiths, cultures, names and ethnicities - Typical


def main():
    with open('input.txt', 'r') as input_file:
        input_file_stripped = input_file.read().replace('\n', ' ')
        input_file.close()

        # needed for later
        pathname = os.path.dirname(sys.argv[0])

        # Personality traits
        personality_traits, seperator, rest_of_everything = \
            input_file_stripped.partition('#Personality_Traits_end_here')

        personality_traits_list = list(personality_traits.split(" "))
        personality_traits_list.pop()  # need to remove last element from the list otherwise there is random ' ' element

        # Education Traits
        education_traits, seperator, rest_of_everything = \
            rest_of_everything.partition('#Education_traits_end_here')

        education_traits_list = list(education_traits.split(" "))
        education_traits_list = education_traits_list[1:-1]  # same here but also for beginning

        # Congenital Traits
        cogenital_traits, seperator, rest_of_everything = \
            rest_of_everything.partition('#Cogenital_traits_end_here')

        cogenital_traits_list = list(cogenital_traits.split(" "))
        cogenital_traits_list = cogenital_traits_list[1:-1]

        # Physical Traits
        physical_traits, seperator, rest_of_everything = \
            rest_of_everything.partition('#Physical_traits_end_here')

        psysical_traits_list = list(physical_traits.split(" "))
        psysical_traits_list = psysical_traits_list[1:-1]

        # Lifestyle Traits
        lifestyle_traits, seperator, rest_of_everything = \
            rest_of_everything.partition('#Lifestyle_traits_end_here')

        lifestyle_traits_list = list(lifestyle_traits.split(" "))
        lifestyle_traits_list = lifestyle_traits_list[1:-1]

        # Commander Traits
        commander_traits, seperator, rest_of_everything = \
            rest_of_everything.partition('#Commander_traits_end_here')
        commander_traits_list = list(commander_traits.split(" "))
        commander_traits_list = commander_traits_list[1:-1]

        # Infamous Traits
        infamous_traits, seperator, rest_of_everything = \
            rest_of_everything.partition('#Infamous_traits_end_here')
        infamous_traits_list = list(infamous_traits.split(" "))
        infamous_traits_list = infamous_traits_list[1:-1]

        # Coping Mechanisms Traits
        cope_traits, seperator, rest_of_everything = \
            rest_of_everything.partition('#Coping_Mechanisms_traits_end_here')
        cope_traits_list = list(cope_traits.split(" "))
        cope_traits_list = cope_traits_list[1:-1]

        # Childhood Traits
        childhood_traits, seperator, rest_of_everything = \
            rest_of_everything.partition('#Childhood_traits_end_here')
        childhood_traits_list = list(childhood_traits.split(" "))
        childhood_traits_list = childhood_traits_list[1:-1]

        # Health Traits
        health_traits, seperator, rest_of_everything = \
            rest_of_everything.partition('#Health_traits_end_here')
        health_traits_list = list(health_traits.split(" "))
        health_traits_list = health_traits_list[1:-1]

        # Bending Traits
        bending_traits, seperator, rest_of_everything = \
            rest_of_everything.partition('#Bending_traits_end_here')
        bending_traits_list = list(bending_traits.split(" "))
        bending_traits_list = bending_traits_list[1:-1]

        # Special Traits (EK, Fire Lord etc)
        special_traits, seperator, rest_of_everything = \
            rest_of_everything.partition('#Special_traits_end_here')
        special_traits_list = list(special_traits.split(" "))
        special_traits_list = special_traits_list[1:-1]

        # Cultures
        cultures, seperator, rest_of_everything = \
            rest_of_everything.partition('#Cultures_end_here')
        cultures_list = list(cultures.split(" "))
        cultures_list = cultures_list[1:-1]

        # faiths
        faiths, seperator, rest_of_everything = \
            rest_of_everything.partition('#Faiths_end_here')
        faiths_list = list(faiths.split(" "))
        faiths_list = faiths_list[1:-1]

        # male_names
        male_names, seperator, rest_of_everything = \
            rest_of_everything.partition('#Male_names_end_here')
        male_names_list = list(male_names.split(" "))
        male_names_list = male_names_list[1:-1]

        # female_names
        fem_names, seperator, rest_of_everything = \
            rest_of_everything.partition('#Female_names_end_here')
        fem_names_list = list(fem_names.split(" "))
        fem_names_list = fem_names_list[1:-1]

        # Random Dynasties
        dynasties, seperator, rest_of_everything = \
            rest_of_everything.partition('#Dynasties_end_here')
        dynasties_list = list(dynasties.split(" "))
        dynasties_list = dynasties_list[1:-1]

        # Set 1st id of char
        char_id_number = 0  # base

        # Sexuality
        sexuality = ["heterosexual", "bisexual", "homosexual", "asexual"]

        # Gender
        gender = ["male", "female"]

    # enter the birth year value

    initialbirthdate = int(input("Input the year the first person of this line was born: "))
    while initialbirthdate < 11:
        initialbirthdate = int(input("value below 11 was imputed, this would cause a negative number, please try again."
                                     "Input the year the first person of this line was born: "))
    initialbirthdatemod = initialbirthdate - 10

    gen_char_gender = random.choice(gender)

    if gen_char_gender == "male":
        spouse_gender = "female"
    else:
        spouse_gender = "male"

    # imput alphanumeric id
    inputed_id = str(input("Input base id of character\nNote:Can be Alphanumerical but this is base id ie:"
                           "[base id] +. [number generated automatically]: "))
    if not inputed_id.isnumeric():
        bool_for_num_id_select = input("You Selected an id which is not numeric.\n"
                                       "Do you want to set numeric id that is after the text?\n"
                                       "Example: Rakurai.(1)<- numeric id\n"
                                       "Yes/no: ")
        if bool_for_num_id_select == "yes" or "y":
            char_id_number = int(input("input numeric is: "))
        else:
            print("You choose to not to input your own numeric id value")

    # rng for birthdate and assigning it to the int datatype

    rng = np.random.default_rng()
    mutwo, sigmatwo = .5, 1  # mean and standard deviation
    birthdate = rng.lognormal(mutwo, sigmatwo, 100)
    birthdate = birthdate.astype(int)

    # adding a random element to the input number to put it over/under a certain value
    # Probably could have used normal instead of log nurmal but bah

    for i in range(0, len(birthdate), 1):
        birthdate[i] = birthdate[i] + initialbirthdate
        flipacoin = random.randint(1, 2)
        randomnumber = random.randint(1, 10)
        if flipacoin == 1:
            birthdate[i] = birthdate[i] - randomnumber

    # makes sure the birthdate doest go waaaay off course from the inital set birthdate

    for i in range(0, len(birthdate), 1):
        if birthdate[i] > initialbirthdate + 25:
            randomgenforbirth = random.randint(1, 10)
            randomgenforbirthcoin = random.randint(1, 2)
            if randomgenforbirthcoin == 1:
                birthdate[i] = initialbirthdate + randomgenforbirth
            else:
                birthdate[i] = initialbirthdate - randomgenforbirth

    # sets the first birthdate as teh entered birthdate

    birthdate[0] = initialbirthdate

    # test print for birthyear
    # print(birthdate)
    # print(birthdate[0])

    # the following is RNG for marriage year

    mumarriage, sigmamarriage = 2.5, .8
    marriageage = rng.lognormal(mumarriage, sigmamarriage, 100)
    marriageage = marriageage.astype(int)

    # I think this was making sure they dont get too old when they're married

    for i in range(0, len(marriageage), 1):
        if marriageage[i] >= 30:
            n = marriageage[i] / 30
            n = int(n)
            n = 30 * n
            n = marriageage[i] - n
            marriageage[i] = n

    # I think this was for allowing really old marriages. Dont recall if it actually did anything

    for i in range(0, len(marriageage), 1):
        randomgenforloweragegrouping = random.randint(1, 5)
        g = randomgenforloweragegrouping
        if g != 5:
            if marriageage[i] >= 18:
                if marriageage[i] >= 28:
                    marriageage[i] = marriageage[i] - 20
                else:
                    marriageage[i] = marriageage[i] - 10
        else:
            continue

    # making the absolute floor for marriage age 16.

    for i in range(0, len(marriageage), 1):
        marriageage[i] = marriageage[i] + 16

    # test print for marriage year
    # print(marriageage)

    # some real jank to get the year they were married
    # Also for a duplicate array to use later since array sizes matter for this
    # I defaulted to a number instead of a variable

    marriageyear = np.zeros(100)
    marriageyear = marriageyear.astype(int)

    for i in range(0, len(birthdate), 2):
        marriageyear[i] = birthdate[i] + marriageage[i]
    marriageyear = marriageyear.astype(int)
    marriageyear = marriageyear[marriageyear != 0]
    marriagedupe = np.repeat(marriageyear, 2)

    # testprint the year
    # print(marriageyear)
    # print(marriagedupe)

    # take marriage year, subtract i+1 from it
    # get the second year for the spouse
    # place it back in the second spot on the array
    # I wrote that in the middle of the night and it kinda makes sense. Kinda.

    for i in range(0, len(marriageyear), 1):
        everyothernumber = (i * 2) + 1
        birthdate[everyothernumber] = marriageyear[i] - marriageage[everyothernumber]

    # test print the revamped birthdate for the spouse
    # print(birthdate)

    # take birthdate and add X amount of years, make sure its actually larger than marriage date

    # RNG for death date. Haha, I used the gaussian function! TAKE THAT!

    mudeath, sigmadeath = 0, 7
    deathdate = np.random.normal(mudeath, sigmadeath, 100)
    deathdate = deathdate.astype(int)

    # setting the default to 65 years after birth

    for i in range(0, len(deathdate), 1):
        deathdate[i] = deathdate[i] + initialbirthdate + 65

    # making sure the marriage year isnt before the deth date. dont want to marry a corpse...

    for i in range(0, len(deathdate), 1):
        if deathdate[i] < marriagedupe[i]:
            newdeath = marriagedupe[i] - deathdate[i]
            deathdate[i] = deathdate[i] + newdeath

    # Cultures traits ect

    # Name
    if gen_char_gender == "male":
        name = random.choice(male_names_list)
        is_female_string = ""
    else:
        name = random.choice(fem_names_list)
        is_female_string = "female = yes"
    # Sexuality
    char_sexuality = random.choice(sexuality)
    # Cultures
    char_culture = random.choice(cultures_list)
    # faith
    char_faith = random.choice(faiths_list)
    # Dynasty
    char_dynn = random.choice(dynasties_list)
    # Education Trait
    char_edu_trait = random.choice(education_traits_list)
    char_edu_trait = f"trait = {char_edu_trait}"
    # Random amount of personality traits
    char_personality_traits_amount = random.choice(range(3, 6))
    char_personality_traits_list = []
    char_personality_traits_list = random.choices(personality_traits_list, k=char_personality_traits_amount)
    for elem in char_personality_traits_list:
        while char_personality_traits_list.count(elem) > 1:
            char_personality_traits_list = list(dict.fromkeys(char_personality_traits_list))
            char_personality_traits_list.append(random.choice(personality_traits_list))
        else:
            break

    if len(char_personality_traits_list) == 4:  # otherwise python shits and dies
        char_personality_traits_list.append("a")
        char_personality_traits_list.append("a")

    elif len(char_personality_traits_list) == 5:
        char_personality_traits_list.append("a")

    if char_personality_traits_amount == 3:
        trait1 = f"trait = {char_personality_traits_list[0]}\n    "
        trait2 = f"trait = {char_personality_traits_list[1]}\n    "
        trait3 = f"trait = {char_personality_traits_list[2]}\n    "
        char_personality_traits_list = trait1 + trait2 + trait3
    elif char_personality_traits_amount == 4:
        trait1 = f"trait = {char_personality_traits_list[0]}\n    "
        trait2 = f"trait = {char_personality_traits_list[1]}\n    "
        trait3 = f"trait = {char_personality_traits_list[2]}\n    "
        trait4 = f"trait = {char_personality_traits_list[3]}\n    "
        char_personality_traits_list = trait1 + trait2 + trait3
    elif char_personality_traits_amount == 5:
        trait1 = f"trait = {char_personality_traits_list[0]}\n    "
        trait2 = f"trait = {char_personality_traits_list[1]}\n    "
        trait3 = f"trait = {char_personality_traits_list[2]}\n    "
        trait4 = f"trait = {char_personality_traits_list[3]}\n    "
        trait5 = f"trait = {char_personality_traits_list[4]}\n    "
        char_personality_traits_list = trait1 + trait2 + trait3 + trait4
    # test print deathdate
    # print(deathdate)

    # the numbers are in, mason, we now know what they mean. Time to type it out.
    # in retrospect I prooooobably should have just put all this info into a higher dimensional array BUT SCREW THAT
    # roll Dob here. FIrst year, then month, then day. If month is 2, then roll d28. otherwise, 30/31 as necessary
    # also check to make sure dod and dom arent conflicting either
    # for now I'll just do spouses instead of iterating on a child
    # and returning the value to the array to do the genertion part all over again.
    # THey can all be split up and called independantly later.

    # ... I could probably make the following code cleanerand shorten it to like, 4 lines of code BUT SCREW THAT

    iterate = 0

    while iterate < 2:
        randombirthmonth = random.randint(1, 12)
        if randombirthmonth == 2:
            randombirthday = random.randint(1, 28)
        elif randombirthmonth == (1, 3, 5, 7, 8, 10, 12):
            randombirthday = random.randint(1, 31)
        else:
            randombirthday = random.randint(1, 30)

        if iterate == 0:
            randommarriagemonth = random.randint(1, 12)
            if randommarriagemonth == 2:
                randommarriageday = random.randint(1, 28)
            elif randommarriagemonth == (1, 3, 5, 7, 8, 10, 12):
                randommarriageday = random.randint(1, 31)
            else:
                randommarriageday = random.randint(1, 30)

        randomdeathmonth = random.randint(1, 12)
        if marriagedupe[iterate] == deathdate[iterate]:
            while randomdeathmonth < randommarriagemonth:
                randomdeathmonth = random.randint(1, 12)

        if randomdeathmonth == 2:
            randomdeathday = random.randint(1, 28)
        elif randomdeathmonth == (1, 3, 5, 7, 8, 10, 12):
            randomdeathday = random.randint(1, 31)
        else:
            randomdeathday = random.randint(1, 30)
        if iterate == 0:
            if marriagedupe[iterate] == deathdate[iterate]:
                while randomdeathday < randommarriageday:
                    if randomdeathmonth == 2:
                        randomdeathday = random.randint(1, 28)
                    elif randomdeathmonth == (1, 3, 5, 7, 8, 10, 12):
                        randomdeathday = random.randint(1, 31)
                    else:
                        randomdeathday = random.randint(1, 30)

        # testprints
        # print(randombirthmonth, randombirthday, randommarriagemonth, randommarriageday, randomdeathmonth, randomdeathday)

        left_curly_brace = "{"
        right_curly_brace = "}"
        if inputed_id.isnumeric():
            char_id = inputed_id
        else:
            char_id_number_stringed = "." + str(char_id_number)
            char_id = inputed_id + char_id_number_stringed

        # Bah this the only way to make this crap append - Typical

        output_line_1 = f"#history \n{char_id} = {left_curly_brace}\n"
        output_line_2 = f"\tname = {name} \n\t{is_female_string}\n\tdisallow_random_traits = yes\n"
        output_line_3 = f"\tculture = {char_culture} \n\tfaith = {char_faith}\n"
        output_line_4 = f"\tdynasty = {char_dynn} \n\tsexuality = {char_sexuality}\n\t"
        output_line_traits = f"#Education\n\t{char_edu_trait}\n\t#Personality\n\t{char_personality_traits_list}"
        output_line_effect = f"{birthdate[iterate]}.{randombirthmonth}.{randombirthday} = {left_curly_brace} " \
                             f"\n\t\tbirth = yes \n\t\teffect = {left_curly_brace} \n\t\t{right_curly_brace} " \
                             f"\n\t{right_curly_brace}\n"
        output_line_marriage = f"\t{marriagedupe[iterate]}.{randommarriagemonth}.{randommarriageday} = {left_curly_brace}" \
                               f"\n\t\teffect = {left_curly_brace} \n\t\t\tmarry = " \
                               f"\n\t\t{right_curly_brace}\n\t{right_curly_brace}\n"
        output_line_death = f"\t{deathdate[iterate]}.{randomdeathmonth}.{randomdeathday} = {left_curly_brace} " \
                            f"\n\t\tdeath = yes \n\t{right_curly_brace} \n{right_curly_brace}\n\n"

        #output_string = [output_line_1, output_line_2, output_line_3, output_line_4, output_line_personality_traits,
                         #output_line_effect, output_line_marriage, output_line_death]
        #output_string = str(output_string)

        if not os.path.exists(pathname + "/output.txt"):
            with open('output.txt', 'x') as output_file:
                print(output_string, file=output_file)
                output_file.close()
        elif os.path.exists(pathname + "/output.txt"):
            # Capture if the user wants to overwrite the whole file
            bool_for_write = input("The Output file already exists do you wish to override it? ")
            # take only the first letter of the answer and convert it to lowercase for easy comparison
            bool_for_write = bool_for_write.strip()[:1].lower()
            #print(bool_for_write)
            if not bool_for_write == "y" and not bool_for_write == "n":
                while not bool_for_write == "y" and not bool_for_write == "n":

                    bool_for_write = input("Invalid answer, please try again."
                                           "The Output file already exists do you wish to override it? ")
                    # take only the first letter of the answer and convert it to lowercase for easy comparison
                    bool_for_write = bool_for_write.strip()[:1].lower()
                    if bool_for_write == "y":
                        with open('output.txt', 'w') as output_file:
                            output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                                    output_line_traits, output_line_effect,
                                                    output_line_marriage,
                                                    output_line_death])
                        break

                    elif bool_for_write == "n":
                        with open('output.txt', 'a') as output_file:
                            output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                                    output_line_traits, output_line_effect,
                                                    output_line_marriage,
                                                    output_line_death])
                        break
                    else:
                        bool_for_write = "Answer is invalid"
            else:
                if bool_for_write == "y":
                    with open('output.txt', 'w') as output_file:
                        output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                               output_line_traits, output_line_effect, output_line_marriage,
                                               output_line_death ])
                        output_file.close()
                elif bool_for_write == "n":
                    with open('output.txt', 'a') as output_file:
                        output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                               output_line_traits, output_line_effect, output_line_marriage,
                                               output_line_death ])
                        output_file.close()
        iterate += 1
        if inputed_id.isnumeric():
            char_id = int(inputed_id)
            char_id += 1
        else:
            char_id_number_stringed = "." + str(char_id_number)
            char_id = inputed_id + char_id_number_stringed
            char_id_number += 1

    # all this crap is to make a table for visual information.
    # count, bins, ignored = plt.hist(birthdate, 100, density=True, align='mid')
    # x = np.linspace(min(bins), max(bins), 10000)
    # pdf = (np.exp(-(np.log(x) - mutwo)**2 / (2 * sigmatwo**2))
    #       / (x * sigmatwo * np.sqrt(2 * np.pi)))
    # plt.plot(x, pdf, linewidth=2, color='r')
    # plt.axis('tight')
    # plt.show()

    # count, bins, ignored = plt.hist(deathdate, 30, density=True)
    # plt.plot(bins, 1/(sigmadeath * np.sqrt(2 * np.pi)) *
    #               np.exp( - (bins - mudeath)**2 / (2 * sigmadeath**2) ),
    #         linewidth=2, color='r')
    # plt.show()


if __name__ == "__main__":
    main()
