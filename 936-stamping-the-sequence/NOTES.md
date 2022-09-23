**Going Backwards**
​
Initially we can find the first match of `stamp` in `target` and replace it with special character, say `*`.
Then we can iterate over `target` again to check if we can match any parts of it with `stamp` ignoring the `*` characters.
We can repeat this process, until we come to a stage when we can't make anymore change to `target`.
If there are remaining characters that are not converted to our special character or the number of turn exceeds `10 * target.length`, we can return [].