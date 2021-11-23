using System;
using System.Collections.Generic;
using System.Text;

namespace BinaryTree.Classes
{
    public class Tree
    {
        private int Height { get; set; } = 0;
        private List<string> Paths { get; set; } = new List<string>();
        public Node Root { get; set; }
        public int Count { get; private set; }

        public Tree(int value)
        {
            Root = new Node(value);
            CalcCount(Root);
        }

        public void DIONoRec(Node n)
        {
            Stack<Node> stack = new Stack<Node>();
            Node c = n;

            while(c != null || stack.Count > 0)
            {
                while (c != null)
                {
                    stack.Push(c);
                    c = c.Left; 
                }
                c = stack.Pop();
                Console.WriteLine(c.Value);

                c = c.Right;
            }
        }

        public void DisplayInorder(Node n)
        {
            DisplayInorderRec(n);
        }

        private void DisplayInorderRec(Node n)
        {
            if(n == null)
            {
                return;
            }
            DisplayInorderRec(n.Left);
            Console.WriteLine(n.Value);
            DisplayInorderRec(n.Right);
        }

        public void DisplayPreOrder(Node n)
        {
            DisplayPreOrderRec(n);
        }

        private void DisplayPreOrderRec(Node n)
        {
            if (n == null)
            {
                return;
            }
            Console.WriteLine(n.Value);
            DisplayPreOrderRec(n.Left);
            DisplayPreOrderRec(n.Right);
        }

        public void DisplayPostOrder(Node n)
        {
            DisplayPostOrderRec(n);
        }

        private void DisplayPostOrderRec(Node n)
        {
            if (n == null)
            {
                return;
            }
            DisplayPostOrderRec(n.Left);
            DisplayPostOrderRec(n.Right);
            Console.WriteLine(n.Value);
        }

        public void DisplayTree(Node n)
        {            
            for (int i = 0; i < Height; i++)
            {
                Display(n, i);
                Console.WriteLine();
            }
        }

        private void CalcCount(Node n)
        {
            if (n == null)
            {
                return;
            }
            Count++;
            CalcCount(n.Left);
            CalcCount(n.Right);
            
        }

        public void Insert(Node newNode)
        {
            if (Count == Math.Pow(2, Height) - 1)
            {
                Node n = Root;
                while(n.Left != null)
                {
                    n = n.Left;
                }
                n.Left = newNode;

                return;
            }
            InsertRek(Root, newNode, 1);
        }

        private void InsertRek(Node n, Node newNode, int h)
        {
           if (n == null && h == Height)
            {
                n = newNode;
                return;
            }
           else if (n == null) { return; }

           InsertRek(n.Left, newNode, h + 1);
           InsertRek(n.Right, newNode, h + 1);


        }

        public int CalcHeight()
        {
            CalcHeightRec(Root, 1);
            return Height;
        }

        private void CalcHeightRec(Node n, int h)
        {
            if (n == null)
            {
                if (Height < h - 1)
                {
                    Height = h - 1;
                }
                return;
            }
            Count++;
            CalcHeightRec(n.Left, h + 1);
            CalcHeightRec(n.Right, h + 1);
        }

        public List<string> GetPath()
        {
            GetPathRec(Root, 1, "");
            return Paths;
        }

        private void GetPathRec(Node n, int h, string path)
        {
            if (n == null)
            {
                return;
            }
            if (Height == h)
            {
                path += n.Value;
                Paths.Add(path);
            }
            GetPathRec(n.Left, h + 1, path + Convert.ToString(n.Value) + "-");
            GetPathRec(n.Right, h + 1, path + Convert.ToString(n.Value)+ "-");
        }

        public void Display(Node n, int lvl)
        {
            DisplayRec(n, lvl, 1);
        }

        private void DisplayRec(Node n, int lvl, int h)
        {
            if (n == null)
            {
                return;
            }

            if (h == lvl + 1)
            {
                Console.WriteLine(n.Value);
            }

            DisplayRec(n.Left, lvl, h + 1);
            DisplayRec(n.Right, lvl, h + 1);
        } 
    }
}
