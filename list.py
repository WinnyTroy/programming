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


