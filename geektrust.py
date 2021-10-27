public class TheTieBreaker {
    private Team batting;
    private Team bowling;
    private Match match;
    
    public TieBreaker(Team batting, Team bowling) {
        this.batting = batting;
        this.bowling = bowling;
        match = new Match(batting, bowling);
    }

    public void playInning(int targetScore, int maxOvers) {
        int score = 0
        for (int over = 0; over < maxOvers; over++) {
            int runs = this.match.simulateOver(score, over, maxOvers, batting.OnStrike());
            score += runs;
        }
        printResult(score, targetScore);
    }

    public void printResult(int score, int target) {
        // logic to decide what need to be the result
        System.out.println(result);
    }
}

public class Match {
    // init state variables
    // constructor etc

    public int simulateOver(int currentScore, int currentOver, int maxOvers, Player player) {
        // logic to simulate an over
        printCommentary(ball, ballScore, player, currentScore);
        // do something
        return runs;
    }
}