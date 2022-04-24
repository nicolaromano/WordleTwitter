def get_wordle_matrix(wordle_tweet: str) -> np.array:
    """ Gets the wordle matrix from a tweet

    Args:
        wordle_tweet (str): The tweet to extract the matrix from

    Returns:
        A matrix containing the combinations of correct/wrong letters for each word
        Wrong letters are represented by 0
        Correct letters in the wrong position are represented by 1
        Correct letters in the correct position are represented by 2
        Unused tries are represented by -1

        TODO: also return a dict with the associate word, the mode (dark/light or high contrast) and any other information
    """

    # Only get the squares
    squares = [chr(c) for c in [11036, 11035, 129000, 128998, 129001, 128999]]

    squares = ''.join(map(str, squares))

    # Only keep the characters that are in the squares string
    wordle_tweet = ''.join(filter(lambda x: x in squares, wordle_tweet))

    # Ensure that the length is a multiple of 5
    if len(wordle_tweet) % 5 != 0:
        # print(f"Skipping Tweet... Length is not a multiple of 5: {len(wordle_tweet)}")
        return None

    # Create the matrix.
    # Check which square we have
    wordle_matrix = np.array([squares.find(w)
                             for w in wordle_tweet]).reshape((-1, 5))
    # We have 2 options per square type (wrong/correct but in the wrong position/correct)
    wordle_matrix //= 2

    # Pad to 5x6 with -1
    if wordle_matrix.shape[0] < 6:
        wordle_matrix = np.pad(wordle_matrix, ((
            0, 6-wordle_matrix.shape[0]), (0, 0)), 'constant', constant_values=-1)

    return wordle_matrix


# Read the csv file into a Pandas dataframe
tweets = pd.read_csv(filename)

matrices = []

for _, t in tqdm(tweets.iterrows(), total=tweets.shape[0]):
   # Get the wordle matrix
    wordle_matrix = get_wordle_matrix(t.tweet)

    if wordle_matrix is not None:
        matrices.append(wordle_matrix)