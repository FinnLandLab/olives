from DataHandlers import *
from Practice import *
from Test import *
from Graphics import *
from Instructions import *
from psychopy import core, event

load_instructions(practice_instructions)
display_practice()

load_instructions(main_instructions)

routine_timer = core.CountdownTimer()
response_timer = core.Clock()
skip = False
for row in participant_table:
    response = ""
    response_time = ""

    response_timer.reset()

    dot_cols_empty = str(row[Constants.DOT_COL]) == 'nan'
    colour_cols_empty = str(row[Constants.COLOUR_COL]) == 'nan'

    circle_visual.fillColor = row[Constants.COLOUR_COL]
    circle_visual.lineColor = row[Constants.COLOUR_COL]

    if not dot_cols_empty:
        dot_circle_visual.pos = Constants.DOT_CORD[row[Constants.DOT_COL]]

    if dot_cols_empty and colour_cols_empty:
        # Square shape should appear
        print 1
        square_visual.draw()
    elif dot_cols_empty:
        # Only big circle appears (colour)
        print 2
        circle_visual.draw()
    elif colour_cols_empty:
        # Only small circle appears (dot)
        print 3
        dot_circle_visual.draw()
    else:
        # Both small and big circles appear (colour and dot)
        print 4
        circle_visual.draw()
        dot_circle_visual.draw()

    routine_timer.add(Constants.DISPLAY_VISUAL_TIME)
    win.flip()

    # Display visuals
    while routine_timer.getTime() > 0:
        if event.getKeys(keyList=Constants.ESCAPE_KEYS):
            core.quit()
        elif event.getKeys(keyList=Constants.SKIP_KEYS):
            skip = True
        elif not response and event.getKeys(keyList=Constants.CIRCLE_KEYS):
            response = Constants.CIRCLE_KEY
            response_time = response_timer.getTime()
        elif not response and event.getKeys(keyList=Constants.SQUARE_KEYS):
            response = Constants.SQUARE_KEY
            response_time = response_timer.getTime()

    win.flip()

    if skip:
        break

    # Remove visuals
    routine_timer.add(Constants.NO_VISUAL_TIME)
    while routine_timer.getTime() > 0:
        if event.getKeys(keyList=Constants.ESCAPE_KEYS):
            core.quit()

    participant_table.addData(Constants.DATA_OUTPUT_COL, response)
    participant_table.addData(Constants.DATA_OUTPUT_RESP_COL, response_time)

    thisExp.nextEntry()

load_instructions(test_instructions)
display_test(dots_test_table)

core.quit()