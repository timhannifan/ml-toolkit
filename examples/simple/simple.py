import sys
sys.path.append('../lib')
sys.path.append('../')
import gridgenerator


def test_grid():
    g = gridgenerator.define_clfs_params('tiny')
    skmodels, params = g
    for k,v in params.items():
        print(k,v)

def main(inpath, outpath, models=None, params_size="test"):

    if models is not None and isinstance(models, list):
        models_to_run = models
    else:
        models_to_run=['RF','LR','DT', 'KNN']

    df = pd.read_csv(inpath)
    print(df.columns)


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Missing parameters, pass inpath and outpath')
        pass
    elif len(sys.argv) == 5:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    elif len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])