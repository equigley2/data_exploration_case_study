***************************
Data cleaning case study
***************************

:Authors: Galvanize DS
:Web site: https://github.com/gSchool/ds-case-study-data-cleaning


Pipline accident data set
-----------------------------------------------

The data are a kaggle data set that was released by the USDOT.

   https://www.kaggle.com/usdot/pipeline-accidents

The `pipeline-accidents.csv` includes a record for each oil pipeline
leak or spill reported to the Pipeline and Hazardous Materials Safety
Administration since 2010. These records include the incident date and
time, operator and pipeline, cause of incident, type of hazardous
liquid and quantity lost, injuries and fatalities, and associated
costs.

   Because these data are in the public domain we ask that your group
   does not use code from any published analyses.  There are
   publically available Jupyter notebooks and more, but please treat
   this as a learning experience.  How far can you get with your
   group's investigative ability?

The goal of this exercise is to take the concepts, tools and
technologies that you have learned up until this point and apply them.
There are not specific objectives except that you will have to present
a summary of your findings at the end of the day.

Coming up with your strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

However you decide to tackle this analysis you will want to
spend some time coming up with a strategy.

  1. You could focus on comparing a subset of states/years/months
  2. You could come up with a series of summary tables
  3. You could investigate a subset of accidents (e.g. the most expensive)
  4. You could try to implement a systematic approach for outlier detection
  5. There are missing values in these data you could compare some different strategies for imputation

Even when you are a seasoned data scientist you will need more than
half of a day to tackle all of these so scope here is important.

Some of the tools that may come in useful here are: correlation
coefficients, groupbys, pivot tables, simple plots from dataframes.

Just in case you are interested in anything time related here are a
couple of lines of code to get you started.

.. code:: python

   df['Date'] = df['Accident Date/Time'].apply(lambda x: (re.split("\s",str(x))[0]))
   df['Month'] = df['Date'].apply(lambda x: (re.split("/",str(x))[0]))
   df['Day'] = df['Date'].apply(lambda x: (re.split("/",str(x))[1]))
   df['Year'] = df['Date'].apply(lambda x: (re.split("/",str(x))[2]))

NBA Basketball data set
-----------------------------------------------
The NBA_data.csv includes average per-game data for all NBA players between the
2013-17 seasons. Features include points, rebounds, blocks, assists, etc. Explore
trends in specific fields over time or compare differences in teams, positions,
and seasons, while utilizing groupbys, pivot tables, and plotting.

Before you dive in, generate some hypotheses or questions you'd like to answer.
Here are some starter questions, although you should generate some of
your own.

    1. Who are the top-10 highest-scoring (`Points`) players in 2016.
    2. Create a table with the average `Points` for each of the five positions on each of the 30 teams (hint: pivot table).
    3. Are players attempting more 3-point shots (`3_Pointers_Attempted`) now as opposed to five years ago?
    4. Is there a trend in `3_Point_%` by position over the last 5 seasons?
    5. Is there a statistically significant difference between the `Field_Goal_%` of each position?
    6. What does the relationship between `Age` and `Points` look like?
    7. Which features are most correlated?

Deliverable
--------------

At the end of the day your group will be expected to present for 5
minutes on your findings.  You can do this directly from your Jupyter
notebooks.

Cover the following in your presentation.

   1. Talk about what you planned to accomplish
   2. How you organized your selves as a team
   3. What you accomplished
   4. Anything new you learned along the way
