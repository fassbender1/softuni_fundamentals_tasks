def check_ticket(ticket: str):
    if len(ticket) != 20:
        return f"invalid ticket"
    win_symbols = {"@", "#", "$", "^"}
    left_part = ticket[:10]
    right_part = ticket[10:]
    for current_win_symbol in win_symbols:
        for length_match in range(10, 5, -1):
            win_symbols_reps = current_win_symbol * length_match
            if win_symbols_reps in left_part and win_symbols_reps in right_part:
                if length_match == 10:
                    return f'ticket "{ticket}" - {length_match}{current_win_symbol} Jackpot!'
                return f'ticket "{ticket}" - {length_match}{current_win_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(check_ticket(current_ticket))
