#!/usr/bin/python
# -*- coding: ascii -*-
import os
import sys


list = [15, 18, 2, 36, 12, 78, 5, 6, 9]


# emulating simple for loop syntax in python
# for x in list:
#     print x

# Getting Average of a list
# Average = sum of all elements / number of elements


# def Average(list):

#     sum = 0
#     for x in list:
#         sum += x
# 	print "Average element is: " +str(sum / float(len(list))

print "Average is : " + str(sum(list) / float(len(list)))
print min(list)
print max(list)


def print_board(board):
    print "The board look like this: \n"

    for i in range(3):
        print " ",
        for j in range(3):
            if board[i * 3 + j] == 1:
                print 'X',

            elif board[i * 3 + j] == 0:
                print 'O',
            else:
                print ' ',

            if j != 2:
                print " | ",

        if i != 2:
            print "-----------------"
        else:
            print


print_board(list)


def display():
    print('   |   |')
    print('-----------')
    print('   |   |')
    print('-----------')
    print('   |   |')


display()


board = [0, 1, 2, 3, 4, 5, 6, 7, 8]


a = '	|	|'
b = '    -----------------'


def show():
    #     for i in range(9):
    #         for a in range(3):
    #             print list[i * 3 + a]

    print a
    print b
    print a
    print b
    print a

# def show():
#     print('   a   a')
#     print('bbbbbbbbbbb')
#     print('   a   a')
#     print('bbbbbbbbbbb')
#     print('   a   a')


show()


board = []
for i in range(9):
    board.append(-1)

print board


for i in range(3):
    for j in range(3):
        print list[i * 3 + j]


a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def drawBoard(a_list):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    # print('   |   |')
    # print(' ' + a_list[7] + ' | ' + a_list[8] + ' | ' + a_list[9])
    print('   |   |')
    print('-----------')
    # print('   |   |')
    # print(' ' + a_list[4] + ' | ' + a_list[5] + ' | ' + a_list[6])
    print('   |   |')
    print('-----------')
    # print('   |   |')
    # print(' ' + a_list[1] + ' | ' + a_list[2] + ' | ' + a_list[3])
    print('   |   |')

drawBoard(a_list)


a = '   |   |'
b = '-----------'


def show():
    print a
    print b
    print a
    print b
    print a

show()


def ui():
    f_name = raw_input('Enter your first name: ')
    l_name = raw_input('Enter your last name: ')
    print('Enter your D.O.B:')
    mo = raw_input("Month: ")
    day = raw_input("Day: ")
    year = raw_input("Year: ")
    print f_name, l_name, "was born on " + mo, day, year


ui()
