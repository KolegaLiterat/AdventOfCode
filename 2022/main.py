from src.dataLoader import DataLoader

def main():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/2022/test_data/day1.txt").load_data()

    print(data)

if __name__ == "__main__":
    main()