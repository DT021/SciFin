# Contributing

Thank you for thinking to contribute!  
(or just being curious about this page :smiley:)

The bigger a project gets, the more necessary to have rules to focus everybody's efforts in an efficient way.
This page gives some guidelines that should be followed to contribute to the project. Obviously, these rules will evolve with time and you are very welcome to suggest modifications of them if you believe they do not make sense.

Please always keep in mind that SciFin serves a certain purpose, and as such its development should make the code move towards that goal. You can read about the objectives of SciFin in the [Readme](https://github.com/SciFin-Team/SciFin/blob/master/README.md) file.

You don't need to be an expert on Python to contribute! However, it is strongly advised to still have a fair knowledge of Python or other programming languages (or at least a strong motivation to learn), and it is recommanded to read in details the following [Python3 Tutorial](https://www.python-course.eu/python3_course.php) before joining the project.


## Reporting Bugs

If you find any bug, please let us know! Here is the procedure to [report an issue](https://docs.github.com/en/github/managing-your-work-on-github/creating-an-issue).


## Suggesting Ideas

If you think some idea or feature could fit well within SciFin, please do not hesitate to send us an email.


## Branches, Commits and Tests

Nobody has a passion for branch creation, merging them, resolving conflicts, etc. So why should we bother? Well, that question has the same answer as why we should eat these non-exciting vegetables like broccoli, cabbage, and spinach... because they are very healthy for us! :smiley: If we don't create branches, one can be almost certain that when the code is too large the modifications that we thought would not affect anyone else will actually disrupt other people's work. **It is thus mandatory to create local development branches, and merge them with the master branch only when we are sure that disruption is minimized.** It is also of great importance to communicate with other developers potentially affected by the changes before proceeding to the branch merger. Each branch should also serve a specific goal reflected by its name. If working on different aspects of the code, it is better to create different branches. In addition, it is **strongly advised to add the author's initials at the begining of the branch name.**

To learn more about branches:
- [managing branches and merging your branch into master](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) (very clear article).
- [basic git commands for branches management](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches).
- [creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

Obviously, there would be no branches without commits, so let's say a few words about them. It is advised to do a commit of your work each time you finish some task that do not involve too many modifications (between 20 and 50 lines of code seem a good estimate, but this really depends on what kind of modifications are being done). **Committing too little or too much both makes a commit useless, so keep an eye on your commits size.** As for the description of your commit, it is advised to tell which function you worked on, in which class or package, and give a short explanation of what you did. Keep in mind that a commit is a message in a bottle for someone who does not know (at all) what you are doing, or for your own self in a not-so-distant future (who may not know at all what you were doing!). From this point of view, it becomes obvious that **a good commit contains the resolution of a specific task**. Thus, a commit should not mix reorganization of code and modification of code. Also, a commit should not combine two unrelated tasks. Thus, when committing, **remember that you will review commits to resolve a problem that appeared from its content.** Finally, it is advized to push commits on the repository's development branch each day to avoid losing too much work in case of problems with local machines.

To learn more about good practice for commits:
- [Git commit rules](https://wiki.openstack.org/wiki/GitCommitMessages#Git_Commit_Good_Practice).

If dealing with branches may sound as appealing as eating broccolis, creating unit tests is probably as boring as washing the dishes! :laughing: But that also is a central aspect of development! **Every function that can have a unit test should see a unit test being written.** The only exceptions for this rule should be plotting functions and some functions which depend on randomly generated values. The best moment to **write that test is right after writing the function, in a new commit**. One should keep in mind that unit testing is like a safeguard and a guarantee of solidity for the future code, hence a **huge saving of time and energy**.

To learn more about unit tests:
- [Python Reference](https://docs.python.org/3/library/unittest.html#) (very well explained).



## Coding Conventions

### Generalities:

The package tries to follow the style guide for Python code [PEP8](https://www.python.org/dev/peps/pep-0008/) and all contributors should try to follow this style. Some parts of the code may not be written in this style and it is also important to maintain the code to uniformize the style on a regular basis.

As for docstrings, the format we try to follow is given by the [numpy doc style](https://numpydoc.readthedocs.io/en/latest/format.html). Again, it is much better to take care of a docstring write after the function is written (and before committing!) than seeing this function misunderstood or unused.


Here are some bulletpoints which are overlaping with the PEP8 style guide which are worth to recall:

- Every function or class we write should have at least a docstring with a short description of its purpose. Doctrings start with """ and end with """.

- Every function or class whose internal operations are not obvious to a "naive reader" should have comments explaining the main operations leading to the result. Comments start with #.

- When a function has several arguments (or when a class has several attributes), it is advised to complete the docstring with the list of arguments (or attributes). The more the arguments (or attributes), the stronger the recommendation to implement that documentation.

- When returned objects are not obvious, a Returns section should be added. A Notes section can also be used to give precisions about the choices made for development and to give references to the reader.

- Do not take any function from someone else, rewrite your methods in your own way. Obviously, for small functions (less than 10 lines) it will be difficult to write a different function, but at least make the function your own. If having no choice but to use someone's else function, give a reliable reference in the "Notes" section.


### Templates:

To help development and avoid too much typing, some templates for functions and classes are provided in the [coding_templates](https://github.com/SciFin-Team/SciFin/blob/master/docs/coding_templates.md) file. Don't hesitate to make use of them!


### Syntax Advice:

Going more into details, some good practice to keep this code clear are the following:

- When deciding for the name of a function, try to follow the pattern method_quantity, for example "historical_variance". Functions should not have capital letters, but classes should (like "TimeSeries").
- Make the name of functions explicit. It is better to lose a bit of time than not being understood.
- For arguments of a function, place most important first and least important last so that from left to write we go from most important to least important arguments.
- Avoid starting description of a function with "Function that ..." or "Method that ...". No need for these introductions. Instead, use the base form of verbs (like "Computes the sum of two elements." or "Plots a function.").
- Avoid starting description of parameters with "The" or "A". Try to include as many types as the function would accept for the argument.
- Use 'DataFrame' to refer to the pandas object and 'data frame' to refer to it in a more general context. Same for classes like 'TimeSeries' with 'time series' or 'CatTimeSeries' with 'categorical time series'.
- Use the base form of verbs in your comments, e.g. 'Create a variable' instead of 'Creates a variable' or (worth) 'Creating a variable'. Imagine you are writing a recipe. Also don't put ":" at the end of comments.
- Cite only reliable sources, preferentially in the "Notes" sections.
- Keep small caps for variables, except for one-letter variable names where it matters less (e.g. N, T).


## Submitting Changes


Please discuss with Fabien Nugier and the developers in SciFin-Team, whose work may be affected by your changes, before you proceed. Good communication is an essential aspect of developing a package together :wink:.



