using System;
using System.Collections.Generic;
using System.Text;

namespace DataStructureDemo.Classes
{
    class DoubleLinkedList
    {
        public DoubleLinkedList()
        {
        }
        public DoubleLinkedNode Head { get; set; }
        public DoubleLinkedNode Last { get; set; }
        public int Length { get; set; } = 0;
        public void DisplayList(DoubleLinkedNode track = null)
        {
            if (track == null)
            {
                track = Head;
            }
            while (track != null)
            {
                Console.Write($"|{track.Value}|-->");
                track = track.Next;
            }
            Console.WriteLine();
        }
        public void DisplayListRev(DoubleLinkedNode track = null)
        {
            if (track == null)
            {
                track = Last;
            }
            while (track != null)
            {
                Console.Write($"|{track.Value}|-->");
                track = track.Prev;
            }
            Console.WriteLine();
        }
    
        public void Add(DoubleLinkedNode newNode)
        {
            if(Head == null)
            {
                Head = newNode;
                Last = Head;
            }
            else
            {
                Last.Next = newNode;
                newNode.Prev = Last;
                Last = newNode;
            }
            Length += 1;

        }
        public void AddFirst(DoubleLinkedNode newNode)
        {
            if (Head == null)
            {
                Head = newNode;
                Last = Head;
            }

            else
            {
                newNode.Next = Head;
                Head.Prev = newNode;
                Head = newNode;
            }

            Length += 1;
        }
        public void AddBeforeValue(DoubleLinkedNode node, DoubleLinkedNode newNode)
        {
            if (Head == null)
            {
                Head = newNode;
                Last = Head;
            }
            else if (Contains(node) == true)
            {
               
                DoubleLinkedNode track = Head;
                while (track.Value != node.Value)
                {
                    track = track.Next;
                }
                newNode.Prev = track.Prev;
                newNode.Prev.Next = newNode;
                track.Prev = newNode;
                newNode.Next = track;
                Length += 1;
            
            }
            else
            {
                Console.WriteLine($"No Node found with {node.Value.GetType()} Value: {node.Value}");
                return;
            }
        }
        public void AddAfterValue(DoubleLinkedNode node, DoubleLinkedNode newNode)
        {
            if (Head == null)
            {
                Head = newNode;
                Last = Head;
            }

            else if (Contains(node) == true)
            {
                DoubleLinkedNode track = Head;
                while (track.Value != node.Value)
                {
                    track = track.Next;
                }
                if(track.Next != null)
                {
                    newNode.Next = track.Next;
                    newNode.Next.Prev = newNode;
                    track.Next = newNode;
                    newNode.Prev = track;
                }
                else
                {
                    track.Next = newNode;
                    newNode.Prev = track;
                    Last = newNode;
                }
                Length += 1;
            }
            else
            {
                    Console.WriteLine($"No Node found with {node.Value.GetType()} Value: {node.Value}");
                    return;
            }
        }
        public void DeleteIndex(int i)
        {
            if(i >= Length)
            {
                Console.WriteLine("Index out of Bound!");
                return;
            }
            if(Length == 1)
            {
                Head = null;
            }
            if (i == 0)
            {
                Head = Head.Next;
            }
            else if(i == Length - 1)
            {
                Last = Last.Prev;
                Last.Next = null;
            }
            else
            {
                DoubleLinkedNode track = Head;
                for (int index = 0; index < i; index++)
                {
                    track = track.Next;
                }
                track.Next.Prev = track.Prev;
                track.Prev.Next = track.Next;
            }
            Length -= 1;


        }
        public void DeleteValue(DoubleLinkedNode node)
        {
            if(Length == 1)
            {
                Head = null;
            }
            if (node.Value == Head.Value)
            {
                Head.Next.Prev = null;
                Head = Head.Next;
            }
            else if (Contains(node) == true)
            {
                DoubleLinkedNode track = Head;
                while (track.Value != node.Value)
                {
                    track = track.Next;
                }
                if (track.Next == null)
                {
                    Last = track.Prev;;
                    track.Prev.Next = null;   
                }
                else
                {
                    track.Next.Prev = track.Prev;
                    track.Prev.Next = track.Next;
                }
            }
            else
            {
                Console.WriteLine($"No Node found with {node.Value.GetType()} Value: {node.Value}");
                return;
            }

            Length -= 1;
        }
        public bool Contains(DoubleLinkedNode node)
        {
            DoubleLinkedNode track = Head;
            while(track != null)
            {
                if(track.Value == node.Value)
                {
                    return true;
                }
                track = track.Next;
            }
            return false;
        }
        public int Find(DoubleLinkedNode node)
        {
            int ind = 0;
            DoubleLinkedNode track = Head;
            while (track != null)
            {
                if (track.Value == node.Value)
                {
                    return ind;
                }
                track = track.Next;
                ind++;
            }
            return -1;
        }
     //public void ConvertToList(int[] arr)
        //{
        //    for (int i = 0; i < arr.Length; i++)
        //    {
        //        Add(new DoubleLinkedNode(arr[i]));
        //    }
            

        //}
        public string[] ConvertToArray()
        {
            string[] arr = new string[Length];
            DoubleLinkedNode track = Head;
            for(int i = 0; i < arr.Length; i++)
            {
                arr[i] = track.Value;
                track = track.Next;
            }
            return arr;
        }
        static public DoubleLinkedList ConvertToList(string[] arr)
        {
            DoubleLinkedList list = new DoubleLinkedList();
            for (int i = 0; i < arr.Length; i++)
            {
                list.Add(new DoubleLinkedNode(arr[i]));
            }
            return list;
        }
        static public string ConvertToDecimal(ref DoubleLinkedNode track2)
        {
            try
            {
                Convert.ToInt32(track2.Value);
            }
            catch
            {
                switch (track2.Value)
                {
                    case "A":
                        track2.Value = "10";
                        break;
                    case "B":
                        track2.Value = "11";
                        break;
                    case "C":
                        track2.Value = "12";
                        break;
                    case "D":
                        track2.Value = "13";
                        break;
                    case "E":
                        track2.Value = "14";
                        break;
                    case "F":
                        track2.Value = "15";
                        break;
                    default:
                        return "Numbers in List were out of range of hexadecimal numbersystem!";
                }
            }
            return track2.Value;
        }
        static public string Addition(int basis, int basisReturn, DoubleLinkedList list1, DoubleLinkedList list2)
        {
            //initialize values
            int number1 = 0;
            int number2 = 0;
            //check numbers in List, if they match with the base of the numbersystem and convert them into decimal numbersystem
            if (basis > 1 && basis < 17)
            {
                DoubleLinkedNode track1 = list1.Head;
                DoubleLinkedNode track2 = list2.Head;
                for (int i = 0; i < list1.Length; i++)
                {
                    if (ConvertToDecimal(ref track1) == "Numbers in List were out of range of hexadecimal numbersystem!")
                    {
                        return "Numbers in List 1 were out of range of hexadecimal numbersystem!";
                    }

                    if (Convert.ToInt32(track1.Value) < 0 || Convert.ToInt32(track1.Value) > basis - 1)
                    {
                        return "Base doesn't match with containig numbers in list 1!";
                    }
                    track1.Value = Convert.ToString(Convert.ToInt32(track1.Value) * Convert.ToInt32(Math.Pow(basis, i)));
                    number1 += Convert.ToInt32(track1.Value);
                    track1 = track1.Next;

                }

                for (int i = 0; i < list2.Length; i++)
                {
                    if (ConvertToDecimal(ref track2) == "Numbers in List were out of range of hexadecimal numbersystem!")
                    {
                        return "Numbers in List 2 were out of range of hexadecimal numbersystem!";
                    }

                    if (Convert.ToInt32(track2.Value) < 0 || Convert.ToInt32(track2.Value) > basis - 1)
                    {
                        return "Base doesn't match with containig numbers in list 2!";
                    }
                    track2.Value = Convert.ToString(Convert.ToInt32(track2.Value) * Convert.ToInt32(Math.Pow(basis, i)));
                    number1 += Convert.ToInt32(track2.Value);
                    track2 = track2.Next;
                }
            }
            else
            {
                Console.WriteLine("Base cannot be smaller than 2 or greater than 16!");
            }

            //converting from decimal system in numbersystem of input(basisReturn)
            if (basisReturn > 1 && basisReturn < 17)
            {
                string res = "";
                int result = number1 + number2;
                while(Convert.ToInt32(result/basisReturn) != 0)
                {
                    int leftover = result % basisReturn;
                    switch (leftover)
                    {
                        case 10:
                            res += "A";
                            break;
                        case 11:
                            res += "B";
                            break;
                        case 12:
                            res += "C";
                            break;
                        case 13:
                            res += "D";
                            break;
                        case 14:
                            res += "E";
                            break;
                        case 15:
                            res += "F";
                            break;
                        default:
                            res += Convert.ToString(leftover);
                            break;    
                    }
                    result = Convert.ToInt32(result / basisReturn);
                }
                res += Convert.ToString(result % basisReturn);
                char[] backRes = res.ToCharArray();
                Array.Reverse(backRes);
                return new string(backRes);
            }
            else
            {
                return "Base of Return cannot be smaller than 2 or greater than 16!";
            }

            
        }
    }
}
