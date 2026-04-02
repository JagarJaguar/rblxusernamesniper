for i in {0..24}; do
  python3 main.py "$i" &
done
wait
