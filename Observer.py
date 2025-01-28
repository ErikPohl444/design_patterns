import abc
"""
Created on Dec 10, 2018

@author: Erik Pohl


"""

"""
The subject object has a one to many dependency on the observers
so that when the subject changes, the observers are automatically
notified
"""


class OnlinetextSubject:
    """
    The subject knows all of its observers.
    It notifies them when it changes state.
    """

    def __init__(self):
        self._online_text_researchers = set()
        self._online_text_contents = None

    def attach(self, research_observer):
        research_observer._online_text = self
        self._online_text_researchers.add(research_observer)

    def detach(self, research_observer):
        research_observer._online_text = None
        self._online_text_researchers.discard(research_observer)

    def _notify(self):
        for observer in self._online_text_researchers:
            observer.update(self._online_text_contents)

    @property
    def subject_state(self):
        return self._online_text_contents

    @subject_state.setter
    def subject_state(self, arg):
        self._online_text_contents = arg
        self._notify()


class ResearchObserver(metaclass=abc.ABCMeta):
    """
    This is an interface for objects which will be notified when the subject
    changes state
    """

    def __init__(self):
        self._online_text = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class OnlineTextResearcherConcreteObserver(ResearchObserver):
    """
    The observer is implemented so that its state changes
    when notified, keeping it aligned with the subject.
    """

    def update(self, arg):
        self._observer_state = arg
        print("state change " + arg)
        # ...


def main():
    my_book_online_text_subject = OnlinetextSubject()
    my_book_researcher_concrete_observer = OnlineTextResearcherConcreteObserver()
    my_book_online_text_subject.attach(my_book_researcher_concrete_observer)
    my_book_online_text_subject.subject_state = 'Chapter 1: The Beginning'
    my_book_online_text_subject.subject_state = 'Chapter 1: A Different Beginning'


if __name__ == "__main__":
    main()
