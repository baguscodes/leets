class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def justify_line(line, width):
            # Distribute extra spaces between words to justify the line
            if len(line) == 1:
                return line[0] + ' ' * (width - len(line[0]))
            total_spaces = width - sum(len(word) for word in line)
            num_words = len(line) - 1
            spaces_between_words = total_spaces // num_words
            extra_spaces = total_spaces % num_words
            justified_line = line[0]
            for i in range(1, len(line)):
                spaces = spaces_between_words + (1 if i <= extra_spaces else 0)
                justified_line += ' ' * spaces + line[i]
            return justified_line

        result = []
        line = [words[0]]
        line_width = len(words[0])

        for word in words[1:]:
            if line_width + len(word) + len(line) <= maxWidth:
                line.append(word)
                line_width += len(word)
            else:
                result.append(justify_line(line, maxWidth))
                line = [word]
                line_width = len(word)

        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)

        return result
