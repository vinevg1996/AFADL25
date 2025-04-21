import re
import math
from tfsm import *
from ttt import *

my_tfsm = TFSM()
my_tfsm.parse_tfsm_file("t_phi_send.tfsm")
ttt = TimedTransitionTour(my_tfsm)
ttt.derive_ttt_template(my_tfsm)
(ttt_left, ttt_mean, ttt_right) = ttt.derive_left_mean_right_ttts(my_tfsm, 1)
print("ttt_left:")
ttt.print_ttt(ttt_left)
print("ttt_mean:")
ttt.print_ttt(ttt_mean)
print("ttt_right:")
ttt.print_ttt(ttt_right)