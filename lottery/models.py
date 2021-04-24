import random


# @debugmethods
class Participant:
    def __init__(self, id, first_name, last_name, weight=1):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._weight = weight

    @property
    def participant_first_name(self):
        return self._first_name

    @property
    def participant_last_name(self):
        return self._last_name

    @property
    def participant_id(self):
        return self._id

    def participant_weight(self):
        return self._weight


class Prize:
    def __init__(self, id, prize_name, prize_amount):
        self._id = id
        self._prize_name = prize_name
        self._prize_amount = prize_amount

    def print_prize_name(self):
        print(self._prize_name)
        return self._prize_name

    @property
    def prize_name(self):
        return self._prize_name

    @property
    def prize_amount(self):
        return self._prize_amount


class Lottery:
    def __init__(self, list_of_participants, list_of_weights, list_of_prizes):
        self._list_of_participants = list_of_participants
        self._list_of_prizes = list_of_prizes
        self._list_of_weights = list_of_weights

    @property
    def print_list_of_participants(self):
        print(self._list_of_participants)
        return self._list_of_participants

    def random_winners_choice(self):
        total_amount_of_prizes = 0
        all_separate_prizes = []
        all_prizes = []

        for x in (range(len(self._list_of_prizes))):
            current_amount = self._list_of_prizes[x].prize_amount
            total_amount_of_prizes += current_amount
            all_prizes.append(self._list_of_prizes[x].prize_name)

        for n in range(0, total_amount_of_prizes):
            try:
                all_separate_prizes.append(all_prizes[n])
            except IndexError:
                all_separate_prizes.append(all_separate_prizes[n - 1])

        winners = random.choices(list(set(self._list_of_participants)),
                                 weights=self._list_of_weights, k=total_amount_of_prizes)
        # print(winners)
        for person in range(len(winners)):
            print(winners[person].participant_id, winners[person].participant_first_name, winners[person].participant_last_name, "has won",
                  all_separate_prizes[person])
        return all_prizes

    all_prizes = property(random_winners_choice)


class Config(object):
    def __init__(self):
        self.verbose = False
