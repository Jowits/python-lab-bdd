from flitter.message import Message


def test_is_by_checks_if_author_matches_user():
    message = Message(author='charlie', text='hello')

    assert message.is_by('charlie')
    assert not message.is_by('bob')


def test_is_in_checks_if_author_in_message_text():
    message = Message(author='Alice', text='Hi @bob')
    
    assert message.is_in('bob')
    
def test_is_in_checks_if_author_is_unique():
    message = Message(author='Alice', text='Hi @bobHope')
    
    assert message.is_in('bob') == False, f"This is the message {message}"
    
def test_if_the_user_is_mentioned_is_in_diffrent_case():
    message = Message(author='Alice', text='I like @bOb a lot')
    
    assert message.is_in('bob')