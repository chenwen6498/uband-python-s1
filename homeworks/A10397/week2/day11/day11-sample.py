#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu

# 1. 把老爸换成老妈，做的时候数一数改了几处代码  【1处】
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码  【1处】
# 
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码  【none】

def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = '老爸 '
  tear_word = 'abandon' #可能会被撕毁的页的key

  print '%s在看一本英文书' % (who)
  if not search('etiquette', book, who):
    tear_mean = book[tear_word]

    del book[tear_word]
    print '%s撕毁了 %s 的页面' % (who, tear_word)

    if search('abash', book, who):
      #老爸黏贴了代码
      book[tear_word] = tear_mean
      print '%s把 %s 的字典页又贴上了' % (who, tear_word)

  lst = ['abase', 'abash']
  for lst_item in lst:
    if search(lst_item, book, who):
      pass #之前卡在这里很久 输出里面一直出现true值 试了很多方法弄不掉 笃长就像天神一样发了一堆消息在群里 太感恩！！


def search(key, book, who):

  if book.has_key(key):
    print '%s查询到了 %s:%s' % (who, key, book[key])
    return True
  else:
    print '%s没有查询到 %s 的意思' %(who, key)
    return False


if __name__ == '__main__':
  homework2()