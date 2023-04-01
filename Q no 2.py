from typing import List, Optional

def earliest_trilogy_year(titles: List[str], years: List[int]) -> Optional[int]:
    # Sort the books by publication year
    sorted_books = sorted(zip(titles, years), key=lambda book: book[1])
    
    # Check for trilogies
    for i in range(len(sorted_books) - 2):
        if sorted_books[i+1][1] == sorted_books[i][1] + 1 and sorted_books[i+2][1] == sorted_books[i][1] + 2:
            return sorted_books[i][1]
    
    # No trilogy found
    return None
