import os , inspect , pytest , session6 , re

README_CONTENT_CHECK_FOR = ['Session6']


#1
def test_readme_exists():
    assert os.path.isfile('README.md') , 'README file is Missing'


#2
def test_readme_formatting():
    f = open('README.md','r')
    content = f.read()
    f.close()
    assert content.count('#') >= 5 , 'Kindly Format the README'


#3
def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


#4
def test_readme_contents():
    f = open("README.md", "r")
    readme_words = f.read().split()
    f.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"


#5
def test_function_had_caps_letters():
    functions = inspect.getmembers( session6, inspect.isfunction )
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


#6
def test_fourspace():
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, "Your code intentation does not follow PEP8 guidelines"


#7
def test_annotation():
    check = session6.poker_star.__annotations__ 
    assert 'no_of_card' in check, 'You Must Define Annotation Properly'


#8
def test_docstring():
    assert 'Input' in session6.poker_star.__doc__ , ' Docstring not Defined'


#9
def test_player_total_card_match():
    with pytest.raises(ValueError):
        session6.poker_star(5,2,['10clubs','9clubs','8clubs','7clubs','6clubs'],['acehearts','kinghearts','queenhearts','jackhearts'])


#10
def test_invalid_no_players():
    with pytest.raises(ValueError):
        session6.poker_star(5,5,['10clubs','9clubs','8clubs','7clubs','6clubs'],['acehearts','kinghearts','queenhearts','jackhearts','10hearts'])


#11
def test_total_generate_cards_without_lambda():
    assert len(session6.generate_cards_without_lambda()) == 52 , 'Card Without 52.... Chaeting!! Cheating !!!'


#12
def test_card_exist_check_without_lambda():
    assert ('Clubs', 'K') in session6.generate_cards_without_lambda() , 'Please Generate All Cards'



#13
def test_total_generate_cards_with_lambda():
    assert len( session6.generate_cards_with_lambda()) == 52 , '......................................'



#14
def test_card_exist_check_with_lambda():
    assert ('Clubs', 'K') in session6.generate_cards_with_lambda() , '-------------------------------------------------'




#15
def test_cards_comparison_between_two_generator():
    with_lambda = session6.generate_cards_without_lambda()
    without_lambda = session6.generate_cards_without_lambda()
    for i in with_lambda:
        assert i in without_lambda , 'There is a mismatch between two card generator'



#16
def test_win_check_in_three_pair_card():
    q1 = session6.poker_star(3,2,['kinghearts','kingspades','9diamonds'],['acehearts','queenclubs','6hearts'])
    assert q1 == 'Player B is winner'



#17
def test_A_winner_in_four_pair_card():
    q1 = session6.poker_star(4,2,['kinghearts','kingspades','9diamonds','8spades'],['acehearts','queenclubs','6hearts','4spades'])
    assert q1 == 'Player B is winner'




#18
def test_A_winner_in_five_pair_card():
    q1 = session6.poker_star(5,2,['kinghearts','kingspades','9diamonds','8spades','4hearts'],['acehearts','queenclubs','6hearts','4spades','2diamonds'])
    assert q1 == 'Player B is winner'



#19
def test_winner_in_five_pair_card():
    q1=session6.poker_star(5,2,['acehearts','queenclubs','6hearts','4spades','2diamonds'],['kinghearts','kingspades','9daimonds','8spades','4hearts'])
    assert q1=='Player B is winner'