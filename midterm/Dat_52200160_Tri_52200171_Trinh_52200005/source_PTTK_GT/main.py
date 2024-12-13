import argparse
import Problem as p

def main():
    parser = argparse.ArgumentParser(description='Run functions.')
    parser.add_argument('--coin_row', action='store_true')
    parser.add_argument('--maximum_flow', action='store_true')
    parser.add_argument('--file', type=str)
    parser.add_argument('--adjacency_matrix', action='store_true')

    args = parser.parse_args()
    
    if args.coin_row:
        Coins = [[],
                [1],
                [5, 5, 10, 100, 10, 5],
                [3, 2, 5, 10, 7],
                [10, 20, 30, 40, 50]]
        c = p.Problem()
        for index, coins in enumerate(Coins, 1):
            c.set_array(coins)
            result = c.coin_row()
            selected = c.extract_selected_coins(coins)
            print(f"\nTrường hợp {index}: {coins}")
            print(f"  Tổng giá trị tối đa: {result}")
            print(f"  Các đồng xu được chọn: {selected}")

    if args.maximum_flow:
        mf = p.Problem()
        mf.set_graph(args.file)
        mf.print()
        flow = mf.shortest_augmenting_path()
        maximum = mf.find_maximum_flow(flow)
        cut_edges = mf.find_minimum_cut(maximum, flow)
        print(f"---Đồ thị sau khi tìm luồng cực đại\n {flow}\n")
        print(f"---Maximum flow: {maximum}\n")
        print(f"---Minimum cut: {cut_edges}\n")

    if args.adjacency_matrix:
        am = p.Problem()
        am.set_graph(args.file)
        am.print()
        adj_matrix, source, sink = am.adjacency_matrix()
        print(f"---Ma trận kề\n {adj_matrix}\n")
        print(f"---Source = {source}, Sink = {sink}")

if __name__ == '__main__':
    main()