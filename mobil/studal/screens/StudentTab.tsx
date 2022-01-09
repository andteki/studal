import { FlatList, StyleSheet, TouchableHighlight } from 'react-native';

import EditScreenInfo from '../components/EditScreenInfo';
import { Text, View } from '../components/Themed';
import { RootTabScreenProps } from '../types';
import { getClassgroups, getStudents } from '../shared/api';
import { useEffect, useState } from 'react';

export default function TabOneScreen({ navigation }: RootTabScreenProps<'TabOne'>) {
  const [classgroups, setClassgroups] = useState([]);
  const [students, setStudents] = useState([]);
  const [selectedClassgroup, setSelectedClassgroup] = useState();
  const [selectedName, setSelectedName] = useState();

  const getStuds = (id: number) => {
    let prom = getStudents(id);    
    prom.then(res => {
        setStudents(res)        
    })
  }

  const getClass = () => {
    let prom = getClassgroups()
    .then(res => {
      setClassgroups(res)
    })
  }

  useEffect(()=> {
    getClass();
  }, [])

  const onClickGroupItem = ( item: any ) => {
    console.log( item.id )
    console.log( item.classgroup)
    setSelectedClassgroup(item.id)
    getStuds(item.id)
    setSelectedName(item.classgroup)
  }
  
  return (
    
    <View style={styles.container}>


      <View style={styles.groupList}>
        <FlatList 
        data={classgroups}        
        renderItem={ ({item})=>(
          <Text style={styles.item} onPress={() => onClickGroupItem(item)}>{item.classgroup}</Text>
        )}        
        />        
      </View>

      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />


      <View style={styles.selectedNameView}>
      <Text style={styles.selectedName}>{selectedName}</Text>
      </View>

      <View style={styles.studList}>
        <FlatList 
        data={students}
        renderItem={ ({item})=>(
          <Text style={styles.item}>{item.name}</Text>
        )}
        />
      </View>
     
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginTop: 10,
  },
  separator: {
    marginVertical: 10,
    height: 1,
    width: '80%',
  },
  item: {
    backgroundColor: 'navy',
    color: 'white',
    padding: 10,
    margin: 8,
  },
  studList: {
    flex: 1,
    width: '100%',
    flexDirection: 'column',
    backgroundColor: 'orange',
  },
  groupList: {

    width: '100%',
    flexDirection: 'column',
    backgroundColor: 'skyeblue',
  },
  getButton: {
    backgroundColor: 'blue',
    marginTop: 10,
    padding: 10,
    borderRadius: 3,
  },
  getButtonText: {
    color: 'white',
    paddingLeft: 10,
    paddingRight: 10,
    fontSize: 22,
  },
  selectedNameView: {

    height: 36,
    backgroundColor: 'orange',
    width: '100%',
  },
  selectedName: {
    textAlign: 'center',
    fontSize: 32,
    color: 'black',

  }
});
