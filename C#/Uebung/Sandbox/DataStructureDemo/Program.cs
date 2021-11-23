using System;
using System.Collections.Generic;
using DataStructureDemo.Classes;

namespace DataStructureDemo
{
    class Program
    {
        static public void SingleMain()
        {
            List<int> list = new List<int>();

            SingleLinkedList slList = new SingleLinkedList();
            SingleLinkedNode n1 = new SingleLinkedNode(2);
            SingleLinkedNode n2 = new SingleLinkedNode(4);
            SingleLinkedNode n3 = new SingleLinkedNode(6);

            slList.Add(n1);
            slList.Add(n2);
            slList.Add(n3);
            slList.DisplayList();
            slList.AddAfter(n1, new SingleLinkedNode(3));
            slList.DisplayList();
            slList.AddStart(new SingleLinkedNode(1));
            slList.DisplayList();
            slList.AddBefore(new SingleLinkedNode(6), new SingleLinkedNode(5));
            slList.DisplayList();
            Console.WriteLine($"Länge{slList.Length}");
            slList.DeleteIndex(0);
            slList.DisplayList();
            slList.DeleteValue(4);
            slList.DisplayList();
            Console.WriteLine($"Länge{slList.Length}");
            Console.WriteLine(slList.Contains(5));
            Console.WriteLine(slList.Contains(4));
            Console.WriteLine(slList.Find(5));
            Console.WriteLine(slList.Find(4));

            slList.Clear();
            slList.DisplayList();
            Console.WriteLine(slList.Length);
        }
        static public void DoubleMain()
        {
            DoubleLinkedList dllist = new DoubleLinkedList();

            DoubleLinkedNode n1 = new DoubleLinkedNode("2");
            DoubleLinkedNode n2 = new DoubleLinkedNode("4");
            DoubleLinkedNode n3 = new DoubleLinkedNode("6");
            DoubleLinkedNode n4 = new DoubleLinkedNode("8");

            dllist.Add(n1);
            dllist.DisplayList();
            dllist.Add(n2);
            dllist.Add(n3);
            dllist.DisplayList();
            dllist.Add(n4);
            dllist.DisplayList();
            dllist.AddFirst(new DoubleLinkedNode("1"));
            dllist.DisplayList();
            dllist.AddAfterValue(n1, new DoubleLinkedNode("3"));
            dllist.DisplayList();
            dllist.AddBeforeValue(n3, new DoubleLinkedNode("5"));
            dllist.DisplayList();
            dllist.DisplayList(dllist.Head);
            dllist.DisplayList(n3);
            dllist.DisplayListRev();
            dllist.DeleteIndex(dllist.Length-1);
            dllist.DisplayList();
            dllist.DeleteIndex(2);
            dllist.DisplayList();
            dllist.DeleteValue(n3);
            dllist.DisplayList();
            Console.WriteLine(dllist.Contains(new DoubleLinkedNode("2")));
            Console.WriteLine(dllist.Contains(new DoubleLinkedNode("12")));
            Console.WriteLine(dllist.Find(new DoubleLinkedNode("4")));
            Console.WriteLine(dllist.Find(new DoubleLinkedNode("12")));
        }
        static public void ArrToList()
        {
            //Fill Array with Random numbers
            Random r = new Random();
            int n = 100;
            int m = 100000;
            string[] arr = new string[n];
            for(int i = 0; i < arr.Length; i++)
            {
                arr[i] = Convert.ToString(r.Next(1, m));
            }

            //Convert Array to DoublelinkedList
            DoubleLinkedList list = DoubleLinkedList.ConvertToList(arr);
            list.DisplayList();
            Console.WriteLine(list.Head.Value);
            Console.WriteLine(list.Last.Value);
            list.DeleteValue(new DoubleLinkedNode(list.Head.Value));
            list.DeleteValue(new DoubleLinkedNode(list.Last.Value));
            list.DisplayList();
            Console.WriteLine(list.Head.Value);
            Console.WriteLine(list.Last.Value);

            string[] a = list.ConvertToArray();
            for(int i = 0; i < a.Length; i++)
            {
                Console.Write($"|{a[i]}");
            }

        }
        static public void AddNumers()
        {
            DoubleLinkedList list1 = new DoubleLinkedList();
            DoubleLinkedList list2 = new DoubleLinkedList();
            //8751
            list1.Add(new DoubleLinkedNode("F"));
            list1.Add(new DoubleLinkedNode("2"));
            list1.Add(new DoubleLinkedNode("2"));
            list1.Add(new DoubleLinkedNode("2"));
            //47
            list2.Add(new DoubleLinkedNode("F"));
            list2.Add(new DoubleLinkedNode("2"));

            Console.WriteLine(DoubleLinkedList.Addition(16, 14, list1, list2)); //8798
        }
        static void Main(string[] args)
        {
            AddNumers();
        }
    }
}
