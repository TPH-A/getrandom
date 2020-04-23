import random, time, pygame, sys, unittest
from pygame.locals import *
class paint_random():
    def __init__(self, xy, fontsize, fontfamily, color, min_number, max_number, write_text, fill_screen):
        self.xy = xy
        self.fontsize = fontsize
        self.fontfamily = fontfamily
        self.color = color
        self.min_number = min_number
        self.max_number = max_number
        self.write_text = write_text
        self.fill_screen = fill_screen
    def show_paint_random(self):
        rand = random.randint(self.min_number, self.max_number)
        randfont = pygame.font.SysFont(self.fontfamily, self.fontsize)
        randfont = randfont.render(self.write_text + str(rand), True, self.color)
        self.fill_screen(randfont, self.xy)
class paint_range_random():
    def __init__(self, xy, fontsize, fontfamily, color, draw_random_numlist, write_text, fill_screen):
        self.xy = xy
        self.fontsize = fontsize
        self.fontfamily = fontfamily
        self.color = color
        self.draw_random_numlist = draw_random_numlist
        self.write_text = write_text
        self.fill_screen = fill_screen
    def show_range_random_list(self):
        range_random_font = pygame.font.SysFont(self.fontfamily, self.fontsize)
        numlist_append = choice(self.draw_random_numlist)
        range_random_font = range_random_font.render(self.write_text + numlist_append, True, self.color)
        self.fill_screen(range_random_font, self.xy)
class sting_random():
    def __init__(self, fitst_text, minnum, maxnum, last_text):
        self.first_text = fitst_text
        self.minnum = minnum
        self.maxnum = maxnum
        self.last_text = last_text
    def outrandomnumber(self):
        randtest = random.randint(self.minnum, self.maxnum)
        random_both = self.first_text + randtest + self.last_text
        print(random_both)
        return random_both
rand_ord = 0
class string_range_random():
    def __init__(self, first_text, range_numlist, last_text):
        self.first_text = first_text
        self.range_numlist = range_numlist
        self.last_text = last_text
    def outrangerandomnumber(self):
        global rand_ord
        rand_ord = random.randint(-1, len(self.range_numlist))
        rd_ord = self.range_numlist[rand_ord]
        random_range_both = self.first_text + rand_ord + self.last_text
        print(random_range_both)
        return random_range_both

unittest.main()

if __name__ == "__main__":
    prtime = time.time()
    prentime = "%.2f" % (time.time() - prtime)
    print(prentime)
    sys.exit()
