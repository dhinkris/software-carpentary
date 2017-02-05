# birth.sh how many births in a state
# Usage: birth.sh [STATE ABBRV.]

cut -f7 $1.txt | tail -n +2 | python add.py