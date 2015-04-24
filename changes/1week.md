## Week 1 Progress

### Virtual Machine

I’ve created the VM (Ubuntu Precise 64bit based), which has required infrastructure inside (MySQL, Python, Django…). This machine could be obtained here: https://github.com/kiote/ansible-django-stack

Repo has a short documentation about how to make this machine run.

### Django App

I’ve created a very beginning of the future app here: https://github.com/kiote/housing_survey

This app also contains some manual steps, which is described in a README.md file.

### Models

For now we have only one model: Newhouse, which corresponds to AHS 2013 National Public Use File (PUF) newhouse.csv

It has 3 fields: CONTROL, DEGREE and METRO3.

## Week2 Plan

Let's suppose we have more or less working infrastructure, so we can spend attention on importing data itself.
Feel a bit uncomfortable with manually creating of Django db-models field, I'm going to auto-generate them in a future, so instead of writing this:

```python
metro3 = models.PositiveSmallIntegerField(db_column = 'METRO3', null = True)
```

there would be rows in [data/columns/newhouse.csv](https://github.com/kiote/housing_survey/blob/master/data/columns/newhouse.csv) file, looking like this:

```
SMSA	CharField	max_length=4
...
over 700 records more
```

and auto-generated models from this csv-file. So only manual step I'll need then is to create this csv files for all models with "field name – field type – params" inside.

Foreign keys and indexes are still needs to be added manually, but this automatization should significantly improve the development speed.

So the actual plan is to auto-import with this method at least one model, possibly more.
