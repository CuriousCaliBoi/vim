"""
Welcome to Vim Practice!
========================

1. Basic Movement
   - Use h, j, k, l to move the cursor
   - Practice moving between words with w, b, e

2. Editing Text
   - Insert mode: i, a, o, O
   - Delete: x, dd, dw
   - Change: c, cc, cw
   - Yank (copy): y, yy, yw
   - Paste: p, P

3. Search and Replace
   - Search forward: /pattern
   - Search backward: ?pattern
   - Replace: :s/old/new/g

4. Working with Multiple Files
   - Open new file: :e filename
   - Split window: :sp, :vsp
   - Switch between windows: Ctrl-w + h, j, k, l

5. Advanced Commands
   - Macros: q{register}, @{register}
   - Marks: m{a-z}, '{a-z}
   - Folding: zf, zo, zc

6. Text Objects
   - Inner word: iw
   - Around word: aw
   - Inner sentence: is
   - Around sentence: as
   - Inner paragraph: ip
   - Around paragraph: ap

7. Visual Mode
   - Character-wise visual mode: v
   - Line-wise visual mode: V
   - Block-wise visual mode: Ctrl-v

8. Command-line Mode
   - Enter command-line mode: :
   - Save file: :w
   - Quit Vim: :q
   - Save and quit: :wq or :x

9. Registers
   - Copy to register: "{register}y
   - Paste from register: "I just changed this ;p"
   - Delete to register: "I just deleted this ;p"
   - View registers: :reg

10. Undo and Redo
    - Undo: u
    - Redo: Ctrl-r

11. Plugins and Customization
    - Installing plugins: Mention popular plugin managers (e.g., Vim-Plug, Vundle)
    - Customizing .vimrc: Brief explanation of how to add personal configurations

12. Vim Modes
    - Normal mode: Default mode for navigation and commands
    - Insert mode: For typing and editing text
    - Visual mode: For selecting text
    - Command-line mode: For entering Ex commands

Practice Area:
--------------
The quick brown fox jumps over the lazy dog.
She sells seashells by the seashore.
How much wood would a woodchuck chuck if a woodchuck could chuck wood?

TODO:
[ ] Delete this line
[ ] Change "fox" to "cat" in the first sentence
[ ] Copy the second sentence and paste it below
[ ] Replace all instances of "wood" with "stone"

Additional Practice Problems:
1. [ ] Insert a new line at the beginning of the Practice Area
2. [ ] Capitalize all words in the second sentence
3. [ ] Delete the third sentence
4. [ ] Indent all lines in the Practice Area by 4 spaces
5. [ ] Join the first two lines into one sentence
6. [ ] Swap the positions of "quick" and "brown" in the first sentence
7. [ ] Convert all lowercase 'a' to uppercase 'A' in the Practice Area
8. [ ] Add line numbers to each line in the Practice Area
9. [ ] Reverse the order of words in the second sentence
10. [ ] Duplicate the entire Practice Area and append it to the end
11. [ ] Use a macro to add a prefix to each line in the Practice Area
12. [ ] Create a vertical split and move half of the Practice Area to the new window
13. [ ] Use text objects to quickly modify content within quotes or parentheses
14. [ ] Practice using marks to quickly jump between different parts of the file
15. [ ] Experiment with different types of registers for copying and pasting

Remember to use Vim commands to practice these tasks!

Happy Vim-ing!
"""
"""
13. Debugging in Vim
    - Using built-in debugger: ':help debug-vim'
    - Integrating with external debuggers (e.g., gdb, pdb)
    - Setting breakpoints: ':breakadd', ':breakdel'
    - Stepping through code: ':next', ':finish'
    - Inspecting variables: ':echo', ':let'

14. Working with Large Codebases
    - Efficient navigation:
      - Using tags: ctags integration, ':tag', 'Ctrl-]'
      - Fuzzy finding: plugins like 'CtrlP' or 'fzf.vim'
    - Code folding: 'za', 'zo', 'zc', 'zR', 'zM'
    - Global search and replace: ':vimgrep', ':cfdo'
    - Project-wide refactoring: plugins like 'vim-refactor'

15. Advanced Vim Features for Large Projects
    - Buffer management: ':ls', ':b', ':bd'
    - Window splits and tabs: ':sp', ':vsp', ':tabnew'
    - Session management: ':mksession', ':source'
    - Autocommands for project-specific settings

Practice Tasks for Large Codebases:
1. [ ] Generate and navigate tags in a multi-file project
2. [ ] Set up a fuzzy finder and practice quick file navigation
3. [ ] Use global search to find all occurrences of a function across files
4. [ ] Refactor a function name across multiple files
5. [ ] Create a custom mapping for switching between related files (e.g., '.h' and '.cpp')
6. [ ] Set up and use persistent undo across sessions
7. [ ] Create a project-specific vimrc using autocommands
8. [ ] Practice using marks to navigate between files
9. [ ] Set up and use 'vim-fugitive' for Git integration in large projects
10. [ ] Customize statusline to show useful project information

Remember to explore plugins and tools that enhance Vim's capabilities for managing and navigating large codebases!
"""