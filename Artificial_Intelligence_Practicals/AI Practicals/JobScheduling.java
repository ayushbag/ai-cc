import java.util.*;

class Job {
    String id;
    int deadline;
    int profit;

    public Job(String id, int deadline, int profit) {
        this.id = id;
        this.deadline = deadline;
        this.profit = profit;
    }
}

public class JobScheduling {
    public static void jobScheduling(Job[] jobs) {
        Arrays.sort(jobs, Comparator.comparingInt(job -> job.deadline));

        int[] maxDeadlines = new int[jobs[jobs.length - 1].deadline + 1];
        Arrays.fill(maxDeadlines, -1);

        int totalProfit = 0;
        for (Job job : jobs) {
            for (int i = job.deadline; i >= 0; i--) {
                if (maxDeadlines[i] == -1) {
                    maxDeadlines[i] = job.profit;
                    totalProfit += job.profit;
                    break;
                }
            }
        }

        System.out.println("Selected Jobs:");
        for (int i = 0; i < maxDeadlines.length; i++) {
            if (maxDeadlines[i] != -1) {
                System.out.println("Deadline " + i + ": Profit " + maxDeadlines[i]);
            }
        }

        System.out.println("Total Profit: " + totalProfit);
    }

    public static void main(String[] args) {
        Job[] jobs = {
                new Job("J1", 2, 100),
                new Job("J2", 1, 19),
                new Job("J3", 2, 27),
                new Job("J4", 1, 25),
                new Job("J5", 3, 15)
        };

        jobScheduling(jobs);
    }
}
