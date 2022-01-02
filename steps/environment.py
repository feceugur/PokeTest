def before_feature(context, feature):
    if feature.name == '':
        context.execute_steps('''
            Given some setup condition that only runs once per feature
              And some other run once setup action
        ''')