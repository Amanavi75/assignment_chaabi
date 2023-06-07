#Q5. Common, Not Common
#Given 2 lists in input. Write a program to return the elements, which are common to both
#lists(set intersection) and those which are not common(set symmetric difference) between the
#lists.

#Input:
#Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword
#Art Online","Bleach","Dragon Ball Z","One Piece"]
#must_watch = ["Full Metal Alchemist","Code Geass","Death
#Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack
#On Titan"]
#f(mainstream, must_watch) should return:
#["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note",
#"One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword
#Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]



def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    not_common_elements = list(set(list1) ^ set(list2))
    return common_elements, not_common_elements

mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]

common, not_common = compare_lists(mainstream, must_watch)
print(common)
print(not_common)
