import InputAdapter, OutputAdapter, Transformer
import sys

def Parser(config):
    #Define the eval environment
    env = {
            'tr': Transformer.Transformer(),
    }
    config = eval(config, env)

    #Load input
    df = getattr(InputAdapter.InputAdapter, config['input'][0])(config['input'][1])

    # Version checking
    if not 'config' in config:
        raise SyntaxError("This doesn't look like config format")
    if config['config'] > 1:
        raise ValueError("This is for a newer config")

    # Run all preprocessing functions
    for function in config['preprocess']:
        #The preprocessing functions change the dataframe, however they don't
        #require assignment of new columns.
        function(df)

    #Run all transformation functions
    for row in config['transformations']:
        #In the new column, run the function and assign the return value.
        df[row[0]] = row[1](df)

    #Output the file
    df = getattr(OutputAdapter.OutputAdapter, config['output'][0])(df, config['output'][1])

def __main__():

    #Uncomment this block to tinker around with the file inside an IDE
    #try:
        #Here we just specify the config file name
    #    Parser(open('Configuration/test01.config', 'r').read())
    #except Exception as e:
    #    print(sys.argv[0] + ': ' + e.__class__.__name__ + ': ' + str(e), file=sys.stderr)


     try:
         Parser(open(sys.argv[1], 'r').read())
     except Exception as e:
         raise
         print(sys.argv[0] + ': ' + e.__class__.__name__ + ': ' + str(e), file=sys.stderr)
         sys.exit(1)

if __name__ == '__main__':
    __main__()