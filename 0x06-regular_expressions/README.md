## 0x06-regular_expressions

**0-simply_match_school.rb**<br>
* Regular expression must match School

**1-repetition_token_0.rb**<br>
* Regular expression must match a couple cases
* **n{X,Y}**	Matches any string that contains a sequence of X to Y n's

**2-repetition_token_1.rb**<br>
* Regular expression must match a couple cases
* **n?**	Matches any string that contains zero or one occurrences of n

**3-repetition_token_2.rb**<br>
* Regular expression must match a couple cases
* **hbt{1,}n**

**4-repetition_token_3.rb**<br>
* Regular expression must match a couple cases
* Regex does not contain square brackets
* **^(?!hbon$).***

**5-beginning_and_end.rb**<br>
* The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
* **^h.n$**

**6-phone_number.rb**<br>
* **(?<!\d)(\d{10})(?!\d)**
* Regular expression must match a 10 digit phone number
* (?<!\d) is a negative lookbehind assertion, which checks that there is no digit immediately before the match.
* (\d{10}) matches exactly 10 consecutive digits and captures them in a group.
* (?!\d) is a negative lookahead assertion, which checks that there is no digit immediately after the match.

**7-OMG_WHY_ARE_YOU_SHOUTING.rb**<br>
* The regular expression only matches: capital letters
* [A-Z]

**100-textme.rb**
The script should output: [SENDER],[RECEIVER],[FLAGS]
* The sender phone number or name (including country code if present)
* The receiver phone number or name (including country code if present)
* The flags that were used
