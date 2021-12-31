import { FlatList, StyleSheet, TouchableHighlight } from 'react-native';

import EditScreenInfo from '../components/EditScreenInfo';
import { Text, View } from '../components/Themed';
import { RootTabScreenProps } from '../types';
import { getStudents } from '../shared/api';
import { useEffect, useState } from 'react';

export default function TabOneScreen({ navigation }: RootTabScreenProps<'TabOne'>) {
  const [students, setStudents] = useState([]);

  const getStuds = () => {
    let prom = getStudents();    
    prom.then(res => {
        setStudents(res)
    })
  }

  useEffect(()=> {
    getStuds();
  }, [])

  const onGetButton = () => {
    getStuds();
  }
  
  return (
    
    <View style={styles.container}>
     
      <Text style={styles.title}>Tanulók</Text>
      <TouchableHighlight
        style={styles.getButton}
        onPress={onGetButton}
      >
        <Text style={styles.getButtonText}>Tölt</Text>
      </TouchableHighlight>

      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

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
    margin: 8 ,
  },
  studList: {
    flex: 1,
    width: '100%',
    flexDirection: 'column',
    backgroundColor: 'orange',
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
  }  
});
