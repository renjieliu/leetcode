class Solution:
    def minDifficulty(self, jobDifficulty: 'List[int]', d: int) -> int: # RL 20221016 Copied Solution, O( d*n**2 | n*d )
        n = len(jobDifficulty)
        # Edge case: make sure there is at least one job per day
        if n < d:
            return -1

        # Precompute the maximum job difficulty for remaining jobs
        max_job_remaining = jobDifficulty[:]
        for i in range(n - 2, -1, -1):
            max_job_remaining[i] = max(max_job_remaining[i], max_job_remaining[i + 1])

        # Use memoization to avoid repeated computation of min_diff states
        @cache
        def min_diff(i, days_remaining):
            # Base case: finish all remaining jobs in the last day
            if days_remaining == 1:
                return max_job_remaining[i]

            res = float('inf')
            daily_max_job_diff = 0 # keep track of the maximum difficulty for today

            # Iterate through possible starting index for the next day
            # and ensure we have at least one job for each remaining day.
            for j in range(i, n - days_remaining + 1):
                daily_max_job_diff = max(daily_max_job_diff, jobDifficulty[j])
                res = min(res, daily_max_job_diff + min_diff(j + 1, days_remaining - 1))

            return res

        return min_diff(0, d)
    
    
