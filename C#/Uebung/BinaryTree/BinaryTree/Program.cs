using BinaryTree.Classes;
using System;
using System.Collections.Generic;

namespace BinaryTree
{
    class Program
    {
        static void Main(string[] args)
        {
            Tree bTree = new Tree(1);
            Node two = new Node(2);
            Node three = new Node(3);
            Node four = new Node(4);
            Node five = new Node(5);
            Node six = new Node(6);
            Node seven = new Node(7);
            Node eight = new Node(8);
            Node nine = new Node(9);
            Node ten = new Node(10);
            Node elev = new Node(11);


            bTree.Root.Left = two;
            bTree.Root.Right = three;
            two.Left = four;
            two.Right = five;
            three.Left = six;
            three.Right = seven;
            four.Left = eight;
            four.Right = nine;
            seven.Right = ten;
            five.Left = elev;



            int heihgt = bTree.CalcHeight();
            //Console.WriteLine(heihgt);


            //Console.WriteLine("Count");
            //Console.WriteLine(bTree.Count);

            //bTree.Display(two, 2);

            //List<string> paths = bTree.GetPath();
            //foreach (string item in paths)
            //{
            //    Console.WriteLine(item);
            //}

            //bTree.DisplayInorder(two);
            //Console.WriteLine();
            //bTree.DisplayPreOrder(two);
            //Console.WriteLine();
            //bTree.DisplayPostOrder(two);
            bTree.DIONoRec(bTree.Root);
            //bTree.DisplayInorder(bTree.Root);

        }
    }
}
