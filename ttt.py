class TimedTransitionTour:
    def __init__(self, my_tfsm):
        self.template_ttt = list()
        self.covered_trans = dict()
        self.set_sequence = dict()
        self.is_reached_state = dict()
        for state in my_tfsm.tfsm.keys():
            self.set_sequence[state] = list()
            self.is_reached_state[state] = False
        for tr_name in my_tfsm.transition_dict.keys():
            self.covered_trans[tr_name] = False
        return

    def is_there_not_reached_state(self, my_tfsm):
        for state in self.is_reached_state.keys():
            if not(self.is_reached_state[state]):
                return True
        return False

    def return_not_reached_state(self, my_tfsm):
        for state in self.is_reached_state.keys():
            if not(self.is_reached_state[state]):
                return state
        return "error"

    def is_there_not_covered_transition(self, my_tfsm):
        for tr_name in my_tfsm.transition_dict.keys():
            if not (self.covered_trans[tr_name]):
                return True
        return False

    def return_not_covered_transition(self, my_tfsm):
        for tr_name in my_tfsm.transition_dict.keys():
            if not (self.covered_trans[tr_name]):
                return my_tfsm.transition_dict[tr_name]
        return "error"

    def return_next_tran_for_state(self, my_tfsm, state):
        for input in my_tfsm.tfsm[state].keys():
            for timed_guard in my_tfsm.tfsm[state][input].keys():
                curr_tr = my_tfsm.tfsm[state][input][timed_guard]
                if not self.covered_trans[curr_tr.transition_name]:
                    return curr_tr
        return None

    def derive_set_seq(self, my_tfsm):
        queue = [(str(my_tfsm.initial_state), [])]
        self.is_reached_state[my_tfsm.initial_state] = True
        self.set_sequence[my_tfsm.initial_state] = []
        while len(queue) > 0:
            (state, seq) = queue.pop()
            for input in my_tfsm.tfsm[state].keys():
                for timed_guard in my_tfsm.tfsm[state][input].keys():
                    tran = my_tfsm.tfsm[state][input][timed_guard]
                    if not self.is_reached_state[tran.end_state]:
                        new_seq = list(seq)
                        new_seq.append(tran.transition_name)
                        queue.append((tran.end_state, new_seq))
                        self.is_reached_state[tran.end_state] = True
                        self.set_sequence[tran.end_state] = list(new_seq)
        return

    def derive_ttt_template(self, my_tfsm):
        self.derive_set_seq(my_tfsm)
        while self.is_there_not_covered_transition(my_tfsm):
            template_seq = list()
            tran = self.return_not_covered_transition(my_tfsm)
            for tr_name in self.set_sequence[tran.start_state]:
                template_seq.append(tr_name)
            template_seq.append(tran.transition_name)
            for tr_name in template_seq:
                self.covered_trans[tr_name] = True
            state = str(tran.end_state)
            deadlock_flag = False
            while not deadlock_flag:
                curr_tr = self.return_next_tran_for_state(my_tfsm, state)
                if curr_tr is None:
                    deadlock_flag = True
                else:
                    template_seq.append(curr_tr.transition_name)
                    self.covered_trans[curr_tr.transition_name] = True
                    state = str(curr_tr.end_state)
            self.template_ttt.append(list(template_seq))
        return
