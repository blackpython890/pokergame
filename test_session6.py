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
def test_playner_total_card_match():
    with pytest.raises(ValueError):
        session6.poker_star(5,2,['10clubs','9clubs','8clubs','7clubs','6clubs'],['acehearts','kinghearts','queenhearts','jackhearts'])